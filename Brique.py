# """
# TP4 - Casse-brique
# Fichier Affichage

# Date : 15/10/2026
# Version : v1
# Auteur : Adel et Nessim

# Objectif : 

# To do :
# """

import random


class Brique:
    """Crée les briques et conserve leurs types."""

    def __init__(self, canvas):
        self.canvas = canvas
        self.briques = []
        self.types = {}

        emplacements = [
            (ligne, colonne)
            for ligne in range(4)
            for colonne in range(9)
        ]

        case_vie, case_score = random.sample(emplacements, 2)

        for ligne, colonne in emplacements:
            x = 10 + colonne * 65
            y = 50 + ligne * 25

            if (ligne, colonne) == case_vie:
                type_brique = "vie"
                couleur = "purple"

            elif (ligne, colonne) == case_score:
                type_brique = "score_bonus"
                couleur = "orange"

            else:
                type_brique = "normale"
                couleur = "green"

            brique = self.canvas.create_rectangle(
                x, y, x + 54, y + 20,
                fill=couleur,
                outline="black"
            )

            self.briques.append(brique)
            self.types[brique] = type_brique

    def detruire(self, identifiant):
        """Supprime une brique et renvoie son type."""
        type_brique = self.types.pop(identifiant)
        self.briques.remove(identifiant)
        self.canvas.delete(identifiant)

        return type_brique
