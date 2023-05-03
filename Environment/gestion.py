from Map.generation import *
from Environment.case_occupe import *

def kill(perso):
    """Tue tous les perso définis en entrée"""
    for position in map:
        if map[position]["objet"] == perso:
            map[position] = {"objet":"grass","IDENTIFIANT":"grass123"}

def reset_camp():
    """Met à jour les camps"""
    #Liste des camps de tous les personnages

    liste_id = all_player(param=["player_red","player_blue"])

    #Fais spawn les perso bb dans leurs nouveaux campements
    for perso in campement:
        if not campement[perso]["active"] and campement[perso]["parent"] in liste_id:
            campement[perso]["active"] = True  #On active le campement (permet de l'afficher)
            map[campement[perso]["position"] ]= campement[perso]["baby"]
            campement[perso]["baby"] = False

    liste_id = all_player(param=["player_red","player_blue"])

    #Supprime les camps attribué a des persos mort
    for perso in campement.copy():
        if perso not in liste_id:
            del campement[perso] #On supprime son campement


#Donne une position vide au hasard sur la map
def hasard_camp():
    while 1 == 1:
        hasard  = random.randint(0,largeur-1)
        hasard2 = random.randint(0,hauteur-1)
        if map[(hasard,hasard2)]["objet"] == "grass":
            #Camp sur un endroit aléatoire
            return (hasard,hasard2)

#Permet de réinitialiser le nombre de poulet mangé pour tous les personnages
def reset_food():
    for i in map:
        if map[i] in ["player_blue","player_red"]:
            map[i]["FOOD"] = 0
