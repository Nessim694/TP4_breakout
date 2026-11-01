"""
TP4 - Casse-brique
Fichier : Raquette.py

Date : 01/11/2026
Version : v2
Auteurs : Adel et Nessim

Objectif : Dessiner la raquette et assurer son déplacement horizontal au clavier sans sortir du Canvas.

À faire : Permettre éventuellement de modifier les touches.
"""


class Raquette:
    def __init__(self, canvas): 
           self.canvas = canvas
           self.raquette = self.canvas.create_rectangle(250,460,350,475, fill="blue")
           self.vitesse = 15

    def _deplacer(self, event):
        """Déplace la raquette sans dépasser le bord du Canvas."""
        x1, _, x2, _ = self.canvas.coords(self.raquette)
        largeur = int(self.canvas["width"])
        if event.keysym == "Left":
            deplacement = max(-self.vitesse, -x1)
        elif event.keysym == "Right":
            deplacement = min(self.vitesse, largeur - x2)
        else:
            return
        self.canvas.move(self.raquette, deplacement, 0)
