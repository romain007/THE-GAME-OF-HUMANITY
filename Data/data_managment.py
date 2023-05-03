import random
from math import *

#Sert à récupérer des donnés dans un fichier ou à y écrire, tous ceux qui est data
#Fait par ANTOINE

def diviseurs_communs(nombre1, nombre2):
    """Retourne les diviseurs communs entre 2 nombres. En entré les 2 nombres et en sortie une liste de diviseur commun""")
    diviseurs1 = set()
    for i in range(1, nombre1 + 1):
        if nombre1 % i == 0:
            diviseurs1.add(i)

    diviseurs2 = set()
    for i in range(1, nombre2 + 1):
        if nombre2 % i == 0:
            diviseurs2.add(i)

    diviseurs_communs = list(diviseurs1.intersection(diviseurs2))
    return diviseurs_communs


def melange_dico(dictionnaire):
    """Melange un dictionnaire en changeant de position les paires clé/valeurs. Prend en entré un dictionnaire et en sortie le dictionnaire mélangé"""
    # Création d'une liste contenant les paires clé-valeur du dictionnaire
    liste_paires = list(dictionnaire.items())

    # Mélange de la liste
    random.shuffle(liste_paires)

    # Création d'un nouveau dictionnaire avec les paires mélangées
    return dict(liste_paires)

def signe(entry):
    #Retourne le signe de l'entry
    if entry >= 0:
        return 1
    if entry < 0:
        return -1
    
def distance_euclidienne(depart,arrive):
    """Distance euclidienne entre 2 points depart et arrive en entrée"""
    return int(sqrt( (depart[0]-arrive[0])**2 + (depart[1]-arrive[1])**2   ))    



