from Map.generation import *

def kill(perso):
    for position in map:
        if map[position]["objet"] == perso:
            map[position] = {"objet":"grass","IDENTIFIANT":"grass123"}

def camp():
    #Liste des camps de tous les personnages
    liste = []

    #Fait apparaitre les bébé dans leur nouveau camps
    for identifiant in campement:
        if campement[identifiant]["baby"]:
            map[campement[identifiant]["position"]] = campement[identifiant]["baby"]

    for i in map:
        if map[i]["objet"] in ["player_red","player_blue"]:
            liste.append(map[i]["CAMP"])

    #Met a jour la liste des campements en supprimant ceux des persos mort
    for identifiant in campement.copy():
        if campement[identifiant]["position"] not in liste:
            del campement[identifiant]

def place_camp():

    while 1 == 1:
        hasard  = random.randint(0,largeur-1)
        hasard2 = random.randint(0,hauteur-1)
        if map[(hasard,hasard2)]["objet"] == "grass":
            #Camp sur un endroit aléatoire
            return (hasard,hasard2)
        
def reset_food():
    for i in map:
        if map[i] in ["player_blue","player_red"]:
            map[i]["FOOD"] = 0