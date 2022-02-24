# projet_tas_de_sable-
#projet sur la simulation de l’écoulement d’un tas de sable
#########################################
# groupe MIASHS
# Marie NGASSAM
# Sami BOUHAFSI
# Zakariya EL HADJAJI 
# https://github.com/mariengassam/projet_tas_de_sable-#readme
#########################################


#######################
# import des librairies
import tkinter
import random as rd



############################
# Définition des constantes

# hauteur du canevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# taille de la grille
n = 4


# choix des couleurs
COUL_CASE = "red"
COUL_VIDE = "white"


###################m###
# variables globales
grille = []



#######################
# fonctions


"""def config_a ():
liste_initiale = []
for j in range(n):#grande boucle
    grille = []
    for i in range(n):#boucle imbriquée
        tableau.append(N*[0])
    grille.append(tableau)
for col in liste_initiale:
    for elem in col:
        print(elem, end = " ")
    x0,y0=i,j
    x1,y1=(i+1),(y+1)
    canvas.create_rectange()
    canvas"""
####################################
#Configuration vide de grains de sables


global grille

def initialisation():
    """ fonction qui initialise la configuration courante et l’affichage de la grille avec une
configuration vide de grains de sable"""
    for i in range(N):
        grille.append([0]*N) 


def config_couleurs():
    """ fonction qui met à jour l’affichage de la grille à partir de la configuration courante, couleurs=>config"""
    for i in range(N):
        for j in range(N):
            if rd.uniform(0, 4) < P:
                terrain[i][j] = 1
                couleur = COUL_MUR
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 2
                couleur="blue"
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 3
                couleur="yellow"
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 4
                couleur="green"
            else:
                couleur = COUL_VIDE#configuration vide de grain de sable cases blanches
                
            largeur = LARGEUR // N
            hauteur = HAUTEUR // N
            x0, y0 = i * largeur, j * hauteur
            x1, y1 = (i + 1) * largeur, (j + 1) * hauteur
            canvas.create_rectangle((x0, y0), (x1, y1), fill=couleur)

def config_avalanche():
    """calcul d’une configuration aléatoire""""
for i in range (n):
    for j in range(n)
        if grille[i][j]>3
            if i==0 and j==0:
                grille[i][j+1]+=1
                grille[i+1][j]+=1
            if i==0 and j<=n-2 and j>0:
                grille[i][j-1]+=1
                grille[i][j+1]+=1
                grille[i+1][j]+=1
            if i==0 and j==n-1:
                grille[i][j-1]+=1
                grille[i+1][j]+=1
            if i>0 and i<n-2 and j==0:
                grille[i-1][j]+=1
                grille[i+1][j]+=1
                grille[i][j+1]+=1
            if i>0 and i<n-2 and j>0 and j<n-2:
                grille[i][j-1]+=1
                grille[i][j+1]+=1
                grille[i-1][j]+=1
                grille[i+1][j]+=1
            if i>0 and i<n-2 and j==n-1:
                grille[i][j-1]+=1
                grille[i-1][j]+=1
                grille[i+1][j]+=1
            if i==n-1 and j==0:
                grille[i][j+1]+=1
                grille[i-1][j]+=1
            if i==n-1 and j>0 and j<n-2:
                grille[i][j-1]+=1
                grille[i][j+1]+=1
                grille[i-1][j]+=1
            if i==n-1 and j==n-1:
                grille[i][j-1]+=1
                grille[i-1][j]+=1
    

#######################
# programme principal

racine=tk.Tk()
racine.title("Sandpile model")
canvas=tk.canvas(racine, bg="red")# ajout du widget canvas 
button1=tk.button(racine, tex="initialisation" width=LARGEUR, height=HAUTEUR, bg="white", command=config_a)# widget bouton initialisation
button2=tk.button(racine, tex="Avalanche" width=LARGEUR, height=HAUTEUR, bg="white", command=config_a)# widget bouton avalanche
racine.bind("<Button-1>", config_aleatoire)
canvas.bind("Buttton2",config_avalanche)

racine.mainloop()


