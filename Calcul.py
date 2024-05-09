from tkinter import *
import math
 
expression = ""
 
def appuyer(touche):
    global expression
    if touche == "=":
        calculer()
        return
    elif touche == "cos":
        expression += "math.cos("
    elif touche == "sin":
        expression += "math.sin("
    else:
        expression += str(touche)
    equation.set(expression)
 
def calculer():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression=""
 
def effacer():
    global expression
    expression = ""
    equation.set("")
 
if __name__ == "__main__":
    gui = Tk()
 
    # Couleur de fond
    gui.configure(background="#FFFFFF")
 
    # Titre de l'application
    gui.title("Calculatrice")
     
 
    # Tailler de la fenetre
    gui.geometry("239x337")
    gui.minsize(239, 337)
    gui.maxsize(239, 337)
 
    # Variable pour stocker le contenu actual
    equation = StringVar()
 
    # Boite de resultats
    resultat = Label(gui, bg="#FFFFFF", fg="#000000", textvariable=equation, height=2)
    resultat.grid(columnspan=5)
 
    # Boutons
    boutons = [7, 8, 9, "cos", "*", 4, 5, 6,"sin", "-", 1, 2, 3,")", "+", 0, ".", "/","(", "="]
    ligne = 1
    colonne = 0
 
    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#FFFFFF", fg="#000000", height=4, width=6)
        # Rendre le texte cliquable
        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))
       
        b.grid(row=ligne, column=colonne)
 
        colonne += 1
        if colonne == 5:
            colonne = 0
            ligne += 1
   
    # Bouton pour effacer
    b = Label(gui, text="Effacer", bg="#808080", fg="#000000", height=2, width=33)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(columnspan=5)
 
    # Demarrer l'interface graphique
    gui.mainloop()

