from Map.generation import *
vect = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)] #liste toute les directions possibles
def next_to(position,attaque,param=[]):
    """renvoie la liste des 8 cases autour de la case d'entrée.Parametre : la liste des objet a exlure"""
    liste_objet = []
    attaquer = False
    pouleto = False
    for vector in vect:
        new_pos = (position[0] + vector[0],position[1] - vector[1])
        if statistique[new_pos]["objet"] == "food" and attaque != 'False' :
            pouleto  = True
            attaquer = False
            break

        if statistique[new_pos]["objet"] == attaque:
           attaquer = True

    for vector in vect:
        new_pos = (position[0] + vector[0],position[1] - vector[1])
        if attaquer:
           if statistique[new_pos]["objet"] == attaque:
               liste_objet.append(new_pos)
        elif pouleto:
            if statistique[new_pos]["objet"] == "food":
               liste_objet.append(new_pos)
        else:
            if statistique[new_pos]["objet"] not in param:
                liste_objet.append(new_pos)
    
    return liste_objet



