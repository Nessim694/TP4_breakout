# TP4 - Casse-brique

Projet Python / Tkinter - Adel et Nessim - 2026.

## Lancer le jeu

Python 3 avec Tkinter installé :

```bash
python Affichage.py
```

## Règles

- Flèches gauche/droite : déplacer la raquette.
- Démarrer : lancer la balle. Empêcher la balle de tomber en bas.
- Chaque brique verte détruite : **+1 point**.
- Brique orange, placée au hasard : **+6 points au total** (1 normal + 5 bonus).
- Brique violette, placée au hasard : **+1 vie de secours dans la pile**, sans changer le compteur de vies visible.
- Quand la balle tombe, une vie de secours est consommée en priorité. Sinon, le joueur perd une vie.
- Toutes les briques détruites : victoire. Plus aucune vie : défaite.
- À la fin de la partie, une fenêtre permet de rejouer ou de quitter.
- Menu Jeu > Recommencer : remet le score, les vies et tous les bonus à zéro.

## Structures de données demandées

- **Liste** : `Brique.py`, `self.briques` contient les identifiants des briques restantes. `append()` à la création, `remove()` à la destruction.
- **Pile LIFO** : `Pile.py`, `empiler()` / `depiler()` / `est_vide()`. `Affichage.py` stocke les vies de secours. La dernière vie de secours obtenue est utilisée en premier (même si les éléments sont identiques).
- **File FIFO** : `File.py`, `enfiler()` / `defiler()` / `est_vide()`, implémentée avec `collections.deque`. `Affichage.py` y ajoute les événements de score et de vie; elle traite le plus ancien à chaque mise à jour.

## Architecture

- `Affichage.py` : fenêtre Tkinter, affichage des compteurs, gestion de la partie et événements.
- `Balle.py` : déplacement, collisions.
- `Brique.py` : génération aléatoire et liste des briques.
- `Raquette.py` : raquette et déplacements.
- `Pile.py` : structure LIFO.
- `File.py` : structure FIFO.

## Bonnes pratiques

Fonctions courtes, docstrings, imports organisés, indentation à quatre espaces, noms explicites, absence de `while True` bloquant Tkinter, lancement protégé par `if __name__ == "__main__"`.

## Git

Adresse du dépôt Git : **à renseigner avant la remise**.

## Limitations / améliorations possibles

Les collisions utilisent le rectangle englobant de la balle, avec un rebond latéral simplifié. Pour une physique stricte, utiliser une intersection cercle/rectangle et une réflexion vectorielle. Les vitesses ne sont pas normalisées après un rebond sur la raquette.
