"""
TP4 - Casse-brique
Fichier : File.py

Date : 01/11/2026
Version : v2
Auteurs : Adel et Nessim

Objectif : Implémenter une file utilisée pour traiter dans l’ordre les événements de score et de bonus.

À faire : Aucun pour la version actuelle.
"""

from collections import deque


class File:
    """Traite les événements dans leur ordre d'arrivée."""

    def __init__(self):
        self.elements = deque()

    def enfiler(self, element):
        """Ajoute un événement à la fin de la file."""
        self.elements.append(element)

    def defiler(self):
        """Retire et renvoie l'événement le plus ancien, ou None."""
        if self.est_vide():
            return None
        return self.elements.popleft()

    def est_vide(self):
        """Indique si aucun événement n'est en attente."""
        return not self.elements

    def __len__(self):
        return len(self.elements)
