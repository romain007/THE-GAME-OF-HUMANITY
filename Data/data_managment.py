import random
from math import *

#Sert à récupérer des donnés dans un fichier ou à y écrire, tous ceux qui est data
#Fait par ANTOINE

def lire(ligne,fichier):
    """ retourne le contenu de la ligne "i" du fichier spécifié, renvoie False si la ligne est vide """
    
    with open(fichier,'r') as file:
        line_content = file.readlines()[ligne-1]
        if line_content == '':
            return False
        return line_content
        
def ecrire(ligne,contenu,fichier):
    """écrit à la ligne "i" dans le fichier spécifié avec le contenu entré"""
    
    with open(fichier,'r') as file:
        file_content = file.readlines()
        file_content[ligne-1] = str(contenu)
        file_content = ''.join(file_content)
    with open(fichier,'w') as file:
        file.write(file_content)

def diviseurs_communs(nombre1, nombre2):
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

    # Création d'une liste contenant les paires clé-valeur du dictionnaire
    liste_paires = list(dictionnaire.items())

    # Mélange de la liste
    random.shuffle(liste_paires)

    # Création d'un nouveau dictionnaire avec les paires mélangées
    return dict(liste_paires)

def signe(entry):
    if entry >= 0:
        return 1
    if entry < 0:
        return -1
    
def distance_euclidienne(depart,arrive):
    return int(sqrt( (depart[0]-arrive[0])**2 + (depart[1]-arrive[1])**2   ))    



