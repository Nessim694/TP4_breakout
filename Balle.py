"""
TP4 - Casse-brique
Fichier : Balle.py

Date : 08/10/2026
Version : v2
Auteurs : Adel et Nessim

Objectif : Gérer la position, les rebonds sur les murs, la raquette et les briques.

À faire : Améliorer si nécessaire les rebonds dans les coins des briques.
"""


class Balle:
      
    def __init__(self, canvas): 
        self.canvas = canvas
        self.balle = self.canvas.create_oval(290, 425, 310, 445, fill="yellow")
        self.vx = -7
        self.vy = -7
    def _deplacerballe(self) :
        
    
        x1, y1, x2, y2 = self.canvas.coords(self.balle)
        
        largeur = int(self.canvas["width"])

        if x1 <= 0 and self.vx < 0:
            self.vx = -self.vx

        elif x2 >= largeur and self.vx > 0:
            self.vx = -self.vx

        if y1 <= 0 and self.vy < 0:
            self.vy = -self.vy

        self.canvas.move(self.balle, self.vx, self.vy)
    def animation(self, raquette, briques, perdre_vie,scoreplus,victoire):
        self._deplacerballe()
        self.collision(raquette)
        
        if self.collision_briques(briques):
            scoreplus()
            if len(briques.briques)==0:
                victoire()
                return
        if self.vies():
            continuer = perdre_vie()

            if not continuer:
                return

        self.canvas.after(
        20,
        self.animation,
        raquette,
        briques,
        perdre_vie,
        scoreplus,
        victoire
    )


    def collision(self,raquette):
        dx1, dy1, dx2, dy2 = self.canvas.coords(self.balle)
        rx1, ry1, rx2, ry2 = self.canvas.coords(raquette.raquette)
        if(self.vy >0 and dx2 >= rx1 and  dx1 <= rx2 and dy2 >= ry1 and dy1 <ry2):
            self.vy = -self.vy

    
  
    def collision_briques(self, briques):
        """Détecte et détruit une brique touchée."""

        bx1, by1, bx2, by2 = self.canvas.coords(self.balle)

        for identifiant in briques.briques:
            rx1, ry1, rx2, ry2 = self.canvas.coords(identifiant)

            if (bx2 >= rx1 and bx1 <= rx2
                    and by2 >= ry1 and by1 <= ry2):

                ancien_x1 = bx1 - self.vx
                ancien_x2 = bx2 - self.vx

                # Si la balle arrivait depuis un côté
                if ancien_x2 <= rx1 or ancien_x1 >= rx2:
                    self.vx = -self.vx
                else:
                    self.vy = -self.vy

                return briques.detruire(identifiant)

        return None


               
            

    def vies(self):
        x1, y1, x2, y2 = self.canvas.coords(self.balle)
        if(y1>=500):
            return True
        else:
            return False
    def reinitialiser(self):
        print("La balle se réinitialise")
        self.canvas.coords(self.balle, 290, 425, 310, 445)
        self.vx = -7
        self.vy = -7