"""
TP4 - Casse-brique
Fichier : Brique.py

Date : 01/11/2026
Version : v2
Auteurs : Adel et Nessim

Objectif : Créer les briques ordinaires et spéciales, enregistrer leurs identifiants et supprimer les briques détruites.

À faire : Ajouter éventuellement des niveaux et des briques résistantes.
"""


import random


class Brique:
    """Construit une grille avec une brique vie et une brique score."""

    def __init__(self, canvas):
        self.canvas = canvas
        self.briques = []
        # Dictionnaire : retrouver le bonus associé à chaque brique.
        self.types = {}  # Identifiant Canvas -> type de brique
        emplacements = [(ligne, colonne) for ligne in range(4)
                        for colonne in range(9)]
        # Deux positions distinctes choisies au hasard à chaque partie.
        case_vie, case_score = random.sample(emplacements, 2)

        for ligne, colonne in emplacements:
            x = 10 + colonne * 65
            y = 50 + ligne * 25
            if (ligne, colonne) == case_vie:
                type_brique, couleur = "vie", "purple"
            elif (ligne, colonne) == case_score:
                type_brique, couleur = "score_bonus", "orange"
            else:
                type_brique, couleur = "normale", "green"

            identifiant = self.canvas.create_rectangle(
                x, y, x + 54, y + 20, fill=couleur, outline="black"
            )
            # Liste exigée par le TP : on la mettra à jour lors des impacts.
            self.briques.append(identifiant)
            self.types[identifiant] = type_brique

    def detruire(self, identifiant):
        """Supprime une brique et renvoie son type."""
        type_brique = self.types.pop(identifiant)
        self.briques.remove(identifiant)
        self.canvas.delete(identifiant)
        return type_brique
