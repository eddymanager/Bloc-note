import tkinter as tk
from tkinter.colorchooser import askcolor 
from tkinter import messagebox
from tkinter import filedialog
import math
import subprocess

# fonction pour ouvrir un fichier :----------------------------------------------------------------------------------------------------
def ouvrir_fichier():
    fichier = filedialog.askopenfile(defaultextension=".txt" , filetypes=[("Fichiers texte" , ".txt"), ("Tous les fichiers","*.*")]) #ouvrir le fichier avec extention txt
   
    if fichier: #ecraser le nouveau fichier qui a ete ouvert
        editeur.delete(1.0 , tk.END)
        editeur.insert(tk.END, fichier.read())
 
# fonction pour enregistrer un fichier()------------------------------------------------------------------------------------------------
def enregistrer_fichier():
    fichier = filedialog.asksaveasfile(defaultextension=".txt" , filetypes=[("Fichiers texte" , ".txt"), ("Tous les fichiers","*.*")])
    if fichier:
        fichier.write= editeur.get(1.0 , tk.END)
 
#fonction pour enregistrer sous du fichier--------------------------------------------------------------------------------------------------
def enregistrer_fichier_sous():
    fichier = filedialog.asksaveasfile(defaultextension=".txt" , filetypes=[("Fichiers texte" , ".txt"), ("Tous les fichiers","*.*")])
    if fichier:
        fichier.write(editeur.get(1.0, tk.END)) #recupere ce qui est ecris sur l'editeur et l'enregistre et 1.0 cest ligne et colonne
#fonction pour faire copier :--------------------------------------------------------------------------------------------------------------
 
def copier():
    editeur.clipboard_clear()  # Efface le contenu précédent du presse-papiers
    editeur.clipboard_append(editeur.selection_get())  # Copie le texte sélectionné dans le presse-papiers
 
#fonction pour faire coller : ---------------------------------------------------------------------------------
def coller():
    texte_coller = editeur.clipboard_get()  # Récupère le texte actuellement dans le presse-papiers
    editeur.insert(tk.INSERT, texte_coller)  # Insère le texte stocké dans le presse-papiers à la position du curseur

# Fonction pour le choix du couleur :--------------------------------------------------------------------
    
def color_option(editeur):
    # Demander la couleur
    color = askcolor()
    if color:
        # Obtenir la plage de texte sélectionnée
        debut_selection = editeur.index(tk.SEL_FIRST)
        fin_selection = editeur.index(tk.SEL_LAST)

        # Appliquer la couleur à la plage de texte sélectionnée
        editeur.tag_add("colored_text", debut_selection, fin_selection)
        editeur.tag_config("colored_text", foreground=color[1])
# Fonction pour le Style de texte :--------------------------------------------------------------------------

def change_style(editeur, style):
    current_font = editeur.cget("font")
    new_font = (style, 12)
    editeur.configure(font=new_font)
# Fonction pour calculatrice :--------------------------------------------------------------------------------------------------------

def ouvrir_calculatrice():
    #exec(open("calcul.py").read())
    subprocess.Popen(["python", "calcul.py"])

# configuration de la fenêtre principale ------------------------------------------------------------------------------------------
fenetre = tk.Tk()
fenetre.title("Bloc Note groupe 3 IT")

# définissez l'icône de la fenêtre ( https://image.online-convert.com/fr/convertir/png-en-ico ) -------------------------------------
fenetre.iconbitmap ("Icone.ico")


#-------- zone d'édition de texte de texte -----------------------²--------------------------------------------------------- ------------------------
editeur = tk.Text(fenetre)
editeur.pack(expand="true", fill="both")

# menu ---------------------------------------------------------------------------------
menu_bar=tk.Menu(fenetre)
fenetre.config(menu = menu_bar)
menu_fichier = tk.Menu(menu_bar,tearoff=0)
menu_edition = tk.Menu(menu_bar,tearoff=0)
menu_option = tk.Menu(menu_bar,tearoff=0)
menu_outil = tk.Menu(menu_bar,tearoff=0)

menu_bar.add_cascade (label= "fichier", menu = menu_fichier )
menu_bar.add_cascade (label= "edition", menu = menu_edition)
menu_bar.add_cascade (label= "option", menu = menu_option)
menu_bar.add_cascade (label= "outil", menu = menu_outil)

# Options de menu fichier (ouvrir, enregistrer.....)----------------------------------------------------------------

menu_fichier.add_command(label="ouvrir", font =("times new roman", 10), command=ouvrir_fichier)
menu_fichier.add_command(label="enregistrer", font =("times new roman", 10), command=enregistrer_fichier)
menu_fichier.add_command(label="enregistrer sous", font =("times new roman", 10), command=enregistrer_fichier_sous)
menu_fichier.add_separator()
menu_fichier.add_command(label="Quitter", font =("times new roman", 10), command=fenetre.quit)


menu_edition.add_command(label="copier", font =("times new roman", 10), command=copier)
menu_edition.add_command(label="coller", font =("times new roman", 10), command=coller)

# Option de menu pour le style d'ecritue :------------------------------------------------------------------
menu_style = tk.Menu(menu_option, tearoff=0)
menu_option.add_cascade(label="Style", menu=menu_style)

styles = ["Arial", "Times New Roman", "Calibri", "Century Schoolbook", "RomanC" ]
for style in styles :
    menu_style.add_command(label=style, font =("times new roman", 10), command= lambda s=style: change_style (editeur, s))

# Option couleur :-------------------------------------------------

menu_option.add_command(label="Color", font =("times new roman", 10), command=lambda: color_option(editeur))
# Outil calculatrice :-------------------------------------------

menu_outil.add_command(label="calculatrice", font =("times new roman", 10), command=ouvrir_calculatrice)

# lancement de la boucle principale ----------------------------------------
fenetre.mainloop()
