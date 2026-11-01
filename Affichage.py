# """
# TP4 - Casse-brique
# Fichier Affichage

# Date : 08/10/2026
# Version : v1
# Auteur : Adel et Nessim

# Objectif : Fichier qui contient la classe Affichage, qui permet d'afficher l'ensemble du jeu

# To do :pour linstant l'affichage est realisé
# """

##classe brique,classe raquette,classe balle,classe affichage, piles avec les vies et une brique bonus qui s'ajoute a la pile
from Brique import Brique
from Raquette import Raquette
from Balle import Balle
import tkinter as tk
from tkinter import messagebox
class Affichage:
    def __init__(self):
        self._dimension()
        self._forme()
        self._vie()
        self._score()
        self._bouton()

        self.fenetre.bind("<Left>", self.Raquette._deplacer)
        self.fenetre.bind("<Right>", self.Raquette._deplacer)
        
        self.fenetre.mainloop()   
    def _dimension(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("Casse-brique")
        self.canvas = tk.Canvas(
                    self.fenetre,
                    width=600,
                    height=500,
                    bg="black"
                        )
        
        self.fenetre.geometry("600x600")
        self.canvas.pack()
    def _forme(self):
        #Raquette qui est centrée en bas du canvas 
        self.Raquette = Raquette(self.canvas)
        #Balle qui est centrée en bas du canvas au dessus de la raquette
        self.Balle = Balle(self.canvas)
        ## Creation des briques
        self.Brique = Brique(self.canvas)

    def _vie(self):
        self.vie = 3

        self.texte_vies = self.canvas.create_text(
        50, 15,
        text=f"Vies : {self.vie}",
        fill="red",
        font=("Arial", 12)
    )
    def _score(self):
        self.score = 0
        self.score_txt= self.canvas.create_text(
                550, 15,
                text="Score : 0",
                fill="yellow",
                font=("Arial", 12)
                    )   
                            
    def scoreplus(self):
            self.score += 1
            self.canvas.itemconfig(
            self.score_txt,
            text=f"Score : {self.score}"
    )
        
    def _perdre_vie(self):
        self.vie -= 1

        self.canvas.itemconfig(
            self.texte_vies,
            text=f"Vies : {self.vie}"
    )

        if self.vie <= 0:
            self._fin_partie("Défaite")
            return False
        else:
            self.Balle.reinitialiser()
            return True
    def _fin_partie(self,message):
        rejouer = messagebox.askyesno(
        "Fin de partie",
        f"{message}\nVoulez-vous recommencer ?"
    )
        if rejouer:
            self._recommencer()
        else:
            self.fentre.detroy()
    def _victoire(self):
        self._fin_partie("Bravo tu as gagné ")
    def _recommencer(self):
       
    # Supprimer les anciennes formes
        self.canvas.delete("all")

    # Recréer les objets
        self._forme()

    # Réinitialiser vies et score
        self._vie()
        self._score()
        self.fenetre.bind("<Left>", self.Raquette._deplacer)
        self.fenetre.bind("<Right>", self.Raquette._deplacer)

    # Réactiver le bouton Démarrer
        self.bouton_demarrer.config(state="normal")    
    def _bouton(self):
        #Bouton demarrer
        self.bouton_demarrer=tk.Button(self.fenetre,text="demarrer", command=self._demarrer)
        self.bouton_demarrer.pack(padx=100, pady=10)
        #Bouton quitter
        self.bouton_quitter=tk.Button(self.fenetre,text="quitter",command=self.fenetre.destroy)
        self.bouton_quitter.pack()    
    def _demarrer(self):
        print("bouton appuyé")
        self.bouton_demarrer.config(state="disabled")
        self.Balle.animation(
            self.Raquette,
            self.Brique,
            self._perdre_vie,
            self.scoreplus,
            self._victoire
    )           
              
    
            
Affichage()     

