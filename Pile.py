"""
TP4 - Casse-brique
Fichier : Pile.py

Date : 01/11/2026
Version : v2
Auteurs : Adel et Nessim

Objectif : Implémenter une pile utilisée pour conserver les bonus de vies de secours.

À faire : Aucun pour la version actuelle.
"""
class Pile:
    """Stocke des bonus : dernier ajouté, premier retiré."""

    def __init__(self):
         # Une liste Python suffit pour implémenter une pile LIFO.
        self.elements = []

    def empiler(self, element):
        """Ajoute un élément au sommet de la pile."""
        self.elements.append(element)

    def depiler(self):
        """Retire et renvoie le sommet, ou None si la pile est vide."""
        if self.est_vide():
            return None
        return self.elements.pop()

    def est_vide(self):
        """Indique si la pile est vide."""
        return not self.elements

    def __len__(self):
        return len(self.elements)
