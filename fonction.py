# """
# TP4 - Casse-brique
# Fichier classe

# Date : 08/10/2026
# Version : v1
# Auteur : Adel et Nessim

# Objectif : faire un casse brique avec son afficheur tkinter

# To do :pour linstant l'affichage est realisé
# """


import tkinter as tk
class Affichage:
    def __init__(self):
        self._dimension()
        self._forme()
        self._bouton()
        self.fenetre.bind("<Left>", self._deplacer_raquette)
        self.fenetre.bind("<Right>", self._deplacer_raquette)
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
        self.raquette = self.canvas.create_rectangle(250,460,350,475, fill="blue")
        #Balle qui est centrée en bas du canvas au dessus de la raquette
        self.canvas.create_oval(290, 425, 310, 445, fill="yellow")
        ## Boucle qui construit les briques sur 4 lignes et 10 colonnes
        for ligne in range(4):
            for colonne in range(9):
                x = 10 + colonne * 65
                y = 20 + ligne *20
                self.canvas.create_rectangle(x,y,x+54,y+20, fill="green")
                 
    
    def _bouton(self):
        #Bouton demarrer
        self.bouton_demarrer=tk.Button(self.fenetre,text="demarrer")
        self.bouton_demarrer.pack(padx=100, pady=10)
        #Bouton quitter
        self.bouton_quitter=tk.Button(self.fenetre,text="quitter",command=self.fenetre.destroy)
        self.bouton_quitter.pack()               
        self.score = self.canvas.create_text(
            550, 15,
                text="Score : 0",
                fill="yellow",
                font=("Arial", 12)
                )           
         
        
    def _deplacer_raquette(self,event):
               
            x1, y1, x2, y2 = self.canvas.coords(self.raquette)
            if event.keysym == "Left" and x1 > 0:
                self.canvas.move(self.raquette, -10, 0)

            elif event.keysym == "Right" and x2 < 600:
                self.canvas.move(self.raquette, 10, 0)     
            
Affichage()     
