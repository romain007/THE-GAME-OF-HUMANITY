from Map.generation import *
import time
vect = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)] #liste toute les directions possibles


def next_to(position):
    liste = []
    for vector in vect:
        new_pos = (position[0] + vector[0],position[1] - vector[1])
        liste.append(new_pos)
    return liste

def filtre(liste,param,tent=False):
    liste_tent = []
    if tent:
        for i in campement:
            liste_tent.append(campement[i]["position"]) 

    for i in liste.copy():
        if map[i]["objet"] in param or i in liste_tent:
            liste.remove(i)

    if liste == []:
        return False,"NONE"

    return True,liste

def filtre_cible(liste,param):

    save = liste.copy()

    for j in liste.copy():

        if map[j]["objet"] not in param:

            liste.remove(j)

    if liste != []:
        return True,liste
    
    return False,save


def all_player(param=[]):
    liste_id = {}
    #Liste de tous les players
    for position in map:
        if map[position]["objet"] in param :
            liste_id[map[position]["IDENTIFIANT"]] = map[position]["objet"]
    return liste_id    



