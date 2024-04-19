import tkinter as tk
from tkinter import* #importation du module Tkinter
import tkinter.filedialog #importation de filedialog pour pouvoir enregistrer le fichier
#fonction pour ouvrir le fichier a lire
root = Tk() #creation de la fentere initiale
root.title("Mon bloc note")#titre de ma fenetre
root.geometry("980x720") # taille de ma fenetre
root.minsize(460, 360) # taille minimal de la fenetre
chemin_icone = "C:/Users/Mediamonster/Desktop/projet editeur/note.ico"
root.iconbitmap("C:/Users/Mediamonster/Desktop/projet editeur/note.ico")

#zone du texte
editeur = Text(root) # creation du widget texte
editeur.pack(expand="true", fill="both") #permet de remplir le widget texte sur la fenetre de facon vertical et horizontal

#creation du menu
menu_bar = Menu(root) # cette ligne cree un nouveau menu appelé menu_bar associé a la fenetre principale root
root.config(menu=menu_bar) # cette ligne configure la fenetre principale root pour utiliser le menu_bar 
# et attribuer ses proprietes a menu
menu_fichier = Menu(menu_bar) # cette ligne cree un nouveau menu deroulant appelé menu_fichier qui sera placé dans le menu 
#principal menu_bar
menu_bar.add_cascade(label="Fichier", menu=menu_fichier) # cette ligne ajoute un element de menu deroulant 
#avec "fichier " au dessus dumenu principal menu_bar 

#option du menu fichier(ouvrir et enregistrer)
menu_fichier.add_command(label = "ouvrir")
menu_fichier.add_separator()
menu_fichier.add_command(label = "enregistrer ")
menu_fichier.add_separator()
menu_fichier.add_command(label = "Quitter")
