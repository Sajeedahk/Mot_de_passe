# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 13:02:21 2025

@author: sajee_4y670z6
"""

import random
import tkinter as tk

majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscules = "abcdefghijklmnopqrstuvwxyz"
chiffres = "0123456789"
speciaux = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"
caracteres = majuscules + minuscules + chiffres + speciaux

#Génération d'un mot de passe aléatoire sécurisé
def generer_MDP():
    MDP = ""
    for i in range (12):
        MDP += random.choice(caracteres)
    entree.delete(0, tk.END)
    entree.insert(0, MDP)
    message.config(text="Mot de passe généré", fg="blue")
   # print (MDP)
    
#Vérification du mot de passe (s'il respecte toute les caractèristiques)
def verif():
    MDP = entree.get()
    if len(MDP) < 12 :
        message.config(text="Le mot de passe doit contenir au moins 12 caractères.", fg="red")
        return
    
    contient_maj = False
    contient_min = False
    contient_chiffre = False
    contient_spec = False
    for i in MDP:
      if i in majuscules:
          contient_maj = True
      elif i in minuscules:
          contient_min = True
      elif i in chiffres : 
          contient_chiffre = True
      elif i in speciaux : 
          contient_spec = True
          
    if contient_maj and contient_min and contient_chiffre and contient_spec :
        message.config(text="Mot de passe valide", fg="green")
    else :
        message.config(text="Mot de passe invalide. Le mot de passe doit contenir au moins une majuscule, une minuscule, un chiffre et un caractère spécial",fg="red")
        
#Cacher ou afficher le mot de passe entrer       
def toggle_affichage():
    if entree.cget("show") == "":
        entree.config(show="*")  
        bouton_oeil.config(text="voir le mot de passe")  
    else:
        entree.config(show="")   
        bouton_oeil.config(text="cacher le mot de passe") 
        
#Configuration de l'interface

fenetre = tk.Tk()
fenetre.title("Générateur / Vérificateur de mot de passe")
fenetre.geometry("420x250")

titre = tk.Label(fenetre, text="Mot de passe sécurisé", font=("Arial", 14))
titre.pack(pady=10)

entree = tk.Entry(fenetre, show="*", width=35)
entree.pack(padx=5,pady=10)
bouton_oeil = tk.Button(fenetre, text="Voir le mot de passe", command=toggle_affichage, width=20, height=2)
bouton_oeil.pack(side=tk.LEFT, padx=5, pady=5)

bouton_verif = tk.Button(fenetre, text="Vérifier", command=verif, width=15, height=2)
bouton_verif.pack(pady=10)

bouton_gen = tk.Button(fenetre, text="Générer", command=generer_MDP, width=15, height=2)
bouton_gen.pack(pady=5)

message = tk.Label(fenetre, text="", font=("Arial", 10))
message.pack(pady=10)

fenetre.mainloop()
        

         