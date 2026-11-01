# """
# TP4 - Casse-brique
# Fichier Raquette

# Date : 15/10/2026
# Version : v1
# Auteur : Adel et Nessim

# Objectif : 

# To do :
# """

class Raquette:
    def __init__(self, canvas): 
           self.canvas = canvas
           self.raquette = self.canvas.create_rectangle(250,460,350,475, fill="blue")



    def _deplacer(self,event):
               
        x1, y1, x2, y2 = self.canvas.coords(self.raquette)
        if event.keysym == "Left" and x1 > 0:
                self.canvas.move(self.raquette, -10, 0)

        elif event.keysym == "Right" and x2 < 600:
                self.canvas.move(self.raquette, 10, 0)     
                

