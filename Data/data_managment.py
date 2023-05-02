# 🧱 - Importation des modules :

import random
from math import *

# ⚙ - Fonctions Utilitaires :

def lire(ligne,fichier):
    """Entrée: ligne, fichier
    Sortie: line_content ou False si la ligne est vide 
    > Retourne le contenu de la ligne spécifiée ou False si la ligne est vide."""
    
    with open(fichier,'r') as file:
        line_content = file.readlines()[ligne-1]
        if line_content == '':
            return False
        return line_content
        
def ecrire(ligne,contenu,fichier):
    """Entrée: ligne, contenu, fichier
    Sortie: Null
    > Modifie la ligne spécifiée du fichier spécifié avec le contenu donné."""
    
    with open(fichier,'r') as file:
        file_content = file.readlines()
        file_content[ligne-1] = str(contenu)
        file_content = ''.join(file_content)
    with open(fichier,'w') as file:
        file.write(file_content)

def diviseurs_communs(nombre1, nombre2):
    """Entree: nombre1, nombre2
    Sortie: diviseurs_communs
    > Retourne les diviseurs communs de deux nombres spécifiés."""
    
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
    """Entrée: dictionnaire
    Sortie: dict(liste_paires)
    > Mélange les paires clé/valeur d'un dictionnaire."""
    
    # Création d'une liste contenant les paires clé-valeur du dictionnaire
    liste_paires = list(dictionnaire.items())

    # Mélange de la liste
    random.shuffle(liste_paires)

    # Création d'un nouveau dictionnaire avec les paires mélangées
    return dict(liste_paires)

def signe(entry):
    """Entrée: entry
    Sortie: 1/-1
    > Retourne 1 si le nombre est positif et -1 si le nombre et négatif"""
    if entry >= 0:
        return 1
    if entry < 0:
        return -1
    
def distance_euclidienne(depart,arrive):
    """Entrée: depart,arrive
    Sortie: int(sqrt((depart[0]-arrive[0])**2 + (depart[1]-arrive[1])**2))
    > Retourne la distance euclidienne entre deux points."""
    return int(sqrt((depart[0]-arrive[0])**2 + (depart[1]-arrive[1])**2))    



