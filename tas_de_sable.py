# projet_tas_de_sable-
#projet sur la simulation de l’écoulement d’un tas de sable
#########################################
# groupe MIASHS
# Marie NGASSAM
# Sami BOUHAFSI
# Zakariya EL HADJAJI 
# https://github.com/mariengassam/projet_tas_de_sable-#readme
#########################################


# 1ere etape: créer une interface graphique qui permet d’afficher un canevas et un bouton qui créera la configuration aléatoire;

import tkinter
from tkinter.font import _FontDescription 
racine=tk.Tk()# widget racine
#Creation d'une liste à deux dimension = variable globale 
int global = liste[][]

canvas=tk.canvas(racine, bg="red",)# ajout du widget canvas (permet de dessiner des objets)

button=tk.button()# widget du widget bouton pour la configuration aléatoire

racine.mainloop()#lancement de la boucle principale

#########################################
#Creation de la _Fonction initialisation (etape 3)
#########################################
def Initialisation ():




#creation de la grille
for ligne in range(5):
    for colonne in range(5):
        Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)
