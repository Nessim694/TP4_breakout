"""
TP4 - Casse-brique
Fichier : Affichage.py

Date : 01/11/2026
Version : v2
Auteurs : Adel et Nessim

Objectif : Créer la fenêtre Tkinter, gérer le lancement, les vies, les points, les bonus, la victoire et le redémarrage.

À faire : Tester le jeu sur différents ordinateurs et ajuster la difficulté.
"""


import tkinter as tk
from tkinter import messagebox

from Balle import Balle
from Brique import Brique
from File import File
from Pile import Pile
from Raquette import Raquette


class Affichage:
    """Fenêtre principale et orchestration d'une partie de casse-brique."""

    def __init__(self):
        # Préparer la fenêtre avant de créer les formes sur le Canvas.
        self._dimension()

        # Les deux structures demandées par le TP sont conservées
        # pendant toute la durée de la partie.
        self.pile_bonus = Pile()  # Bonus de vie en réserve : LIFO
        self.file_evenements = File()  # Événements de jeu : FIFO
        # Évite de lancer plusieurs animations si on reclique sur Démarrer.
        self.partie_en_cours = False
        self._after_id = None
        # Chaque classe reçoit le même Canvas pour y dessiner ses éléments.
        self._forme()
        self._vie()
        self._score()
        self._bouton()
        # La méthode intermédiaire cible toujours la raquette actuelle.
        self.fenetre.bind("<Left>", self._touche_raquette)
        self.fenetre.bind("<Right>", self._touche_raquette)
        self.fenetre.mainloop()

    def _dimension(self):
        """Crée la fenêtre et le Canvas."""
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse-brique")
        self.fenetre.resizable(False, False)
        self.canvas = tk.Canvas(
            self.fenetre, width=600, height=500,
            bg="black", highlightthickness=0
        )
        self.canvas.pack()

    def _forme(self):
        """Crée les objets du niveau."""
        self.Raquette = Raquette(self.canvas)
        self.Balle = Balle(self.canvas)
        self.Brique = Brique(self.canvas)

    def _vie(self):
        """Initialise et affiche les vies et le stock de bonus."""
        self.vie = 3
        self.texte_vies = self.canvas.create_text(
            12, 14, text="Vies : 3", anchor="w", fill="red",
            font=("Arial", 12, "bold")
        )
        self.texte_bonus = self.canvas.create_text(
            300, 14, text="Réserve : 0", fill="violet",
            font=("Arial", 12, "bold")
        )

    def _score(self):
        """Initialise et affiche le score."""
        self.score = 0
        self.score_txt = self.canvas.create_text(
            588, 14, text="Score : 0", anchor="e", fill="yellow",
            font=("Arial", 12, "bold")
        )

    def _actualiser_infos(self):
        """Actualise les compteurs sur le Canvas."""
        self.canvas.itemconfig(self.texte_vies, text=f"Vies : {self.vie}")
        self.canvas.itemconfig(
            self.texte_bonus, text=f"Réserve : {len(self.pile_bonus)}"
        )
        self.canvas.itemconfig(self.score_txt, text=f"Score : {self.score}")

    def _bouton(self):
        """Crée les boutons Démarrer et Quitter."""
        zone = tk.Frame(self.fenetre)
        zone.pack(pady=12)
        self.bouton_demarrer = tk.Button(
            zone, text="Démarrer", width=12, command=self._demarrer
        )
        self.bouton_demarrer.pack(side="left", padx=10)
        self.bouton_quitter = tk.Button(
            zone, text="Quitter", width=12, command=self.fenetre.destroy
        )
        self.bouton_quitter.pack(side="left", padx=10)
        # Aide visuelle : les couleurs annoncent les récompenses.
        self.legende = tk.Label(
            self.fenetre,
            text="Vert : +1 point   |   Orange : +6 points   |   Violet : vie de secours",
            font=("Arial", 9)
        )
        self.legende.pack()
        # Menu demandé dans l’énoncé : recommencer ou quitter.
        menu = tk.Menu(self.fenetre)
        menu_jeu = tk.Menu(menu, tearoff=False)
        menu_jeu.add_command(label="Recommencer", command=self._recommencer)
        menu_jeu.add_command(label="Quitter", command=self.fenetre.destroy)
        menu.add_cascade(label="Jeu", menu=menu_jeu)
        self.fenetre.config(menu=menu)

    def _touche_raquette(self, event):
        """Transmet les flèches clavier à la raquette active."""
        self.Raquette._deplacer(event)

    def _demarrer(self):
        """Démarre une seule boucle d'animation."""
        if self.partie_en_cours:
            return
        self.partie_en_cours = True
        self.bouton_demarrer.config(state="disabled")
        self._animation()

    def _animation(self):
        """Déplace la balle, traite les collisions et les événements."""
        if not self.partie_en_cours:
            return
        # Le rappel prévu est en cours : il n’est plus en attente.
        self._after_id = None
        # Une étape de simulation : déplacement, puis collisions.
        self.Balle._deplacerballe()
        self.Balle.collision(self.Raquette)
        type_brique = self.Balle.collision_briques(self.Brique)
        if type_brique is not None:
            # Les événements entrent dans une file FIFO. Un bonus orange
            # vaut 1 point normal + 5 points supplémentaires.
            self.file_evenements.enfiler(("score", 1))
            if type_brique == "vie":
                self.file_evenements.enfiler(("bonus_vie", 1))
            elif type_brique == "score_bonus":
                self.file_evenements.enfiler(("score", 5))

        # Un événement est consommé par image : la file peut donc
        # contenir temporairement plusieurs récompenses.
        self._traiter_evenement()

        if self.Balle.vies():
            if not self._perdre_vie():
                self._fin_partie("Défaite !")
                return

        # Attendre la fin de la file pour créditer aussi le dernier bonus.
        if not self.Brique.briques and self.file_evenements.est_vide():
            self._fin_partie("Victoire !")
            return

        self._after_id = self.fenetre.after(20, self._animation)

    def _traiter_evenement(self):
        """Dépile un événement FIFO à chaque image du jeu."""
        evenement = self.file_evenements.defiler()
        if evenement is None:
            return
        nature, valeur = evenement
        if nature == "score":
            self.score += valeur
        elif nature == "bonus_vie":
            self.pile_bonus.empiler("vie")
        self._actualiser_infos()

    def _perdre_vie(self):
        """Consomme une réserve LIFO ou retire une vie; renvoie True si vivant."""
        # La pile fournit une vie de secours AVANT les vies normales.
        if not self.pile_bonus.est_vide():
            self.pile_bonus.depiler()
        else:
            self.vie -= 1
        self._actualiser_infos()
        if self.vie <= 0:
            return False
        self.Balle.reinitialiser()
        return True

    def _fin_partie(self, message):
        """Arrête l'animation et demande au joueur s'il veut rejouer."""
        # Bloquer la simulation avant d’afficher la boîte de dialogue.
        self.partie_en_cours = False
        self._annuler_animation()
        rejouer = messagebox.askyesno(
            "Fin de partie", f"{message} Score : {self.score}\nRecommencer ?",
            parent=self.fenetre
        )
        if rejouer:
            self._recommencer()
        else:
            self.fenetre.destroy()

    def _annuler_animation(self):
        """Annule le prochain appel planifié, s’il existe."""
        if self._after_id is not None:
            self.fenetre.after_cancel(self._after_id)
            self._after_id = None

    def _recommencer(self):
        """Crée une nouvelle partie sans conserver les anciens bonus."""
        self.partie_en_cours = False
        self._annuler_animation()
        # Supprimer les formes de l’ancienne partie puis recréer le niveau.
        self.canvas.delete("all")
        self.pile_bonus = Pile()
        self.file_evenements = File()
        self._forme()
        self._vie()
        self._score()
        self.bouton_demarrer.config(state="normal")


if __name__ == "__main__":
    Affichage()
