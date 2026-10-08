import tkinter as tk
class Affichage:
    def __init__(self):
        self._dimension()
        self._forme()
        self._bouton()
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
        #Raquette
        self.canvas.create_rectangle(250,460,350,475, fill="blue")
        #Balle
        self.canvas.create_oval(290, 425, 310, 445, fill="yellow")
        ##Brique
        for ligne in range(4):
            for colonne in range(10):
                x = 10 + colonne * 59
                y = 20 + ligne * 25

            self.canvas.create_rectangle(
                x, y, x + 54, y + 20,
                fill="green"
            )
    
    def _bouton(self):
        #Bouton demarrer
        self.bouton_demarrer=tk.Button(self.fenetre,text="demarrer")
        self.bouton_demarrer.pack()
        #Bouton quitter
        self.bouton_quitter=tk.Button(self.fenetre,text="quitter",command=self.fenetre.destroy)
        self.bouton_quitter.pack()
        self.fenetre.mainloop()        
    
affichage = Affichage()     
