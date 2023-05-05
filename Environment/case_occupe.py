from Map.generation import *
import time
vect = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)] #liste toute les directions possibles

#Ce module à pour role de renvoyer les cases alentour d'une case, avec plusieurs conditions

def next_to(position):
    """Renvoie en sortie la liste des 8 cases autour d'une position en entrée"""
    liste = []
    for vector in vect:
        new_pos = (position[0] + vector[0],position[1] - vector[1])
        liste.append(new_pos)
    return liste

def filtre(liste,param):
    """Permet de filtrer une liste de case. Par exemple, en appliquant le filtre rock, on n'a en retour que des cases qui ne sont pas occupé par rock"""

    for i in liste.copy():
        if map[i]["objet"] in param :
            liste.remove(i)

    if liste == []:
        return False,"NONE"  #Si il n'y a aucune case correspondante au filtres, renvoie un message d'erreur

    return True,liste

def filtre_cible(liste,param):
    """Filtre une liste de case en entré suivant des paramètres en retournant unquement la liste des objets souhaités. Par exemple, en appliquant le filtre "food", j'obtiens en sortie une liste de case occupé par des poulets"""
    save = liste.copy()

    for j in liste.copy():

        if map[j]["objet"] not in param:

            liste.remove(j)

    if liste != []:
        return True,liste  #Si il n'y a aucune case correspondante au filtres, renvoie la liste initiale
    
    return False,save


def all_player(param=[]):
    """Renvoie en sortie une liste des identifiants de tous les players actuellements en vie"""
    liste_id = {}
    #Liste de tous les players
    for position in map:
        if map[position]["objet"] in param :
            liste_id[map[position]["IDENTIFIANT"]] = map[position]["objet"]
    return liste_id    



