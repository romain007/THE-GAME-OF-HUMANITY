from Map.generation import *
from Environment.case_occupe import *

#Ce module est remplie de fonction annexe, servant à la gestion de l'énergie, des camps, ect...

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

def restart(val=100):
    # Remet à 100 l'energie des persos qui sont rentrés
    for pos in map:
        if map[pos]["objet"] in ["player_red","player_blue"] and pos == map[pos]["CAMP"]:
            map[pos]["ENERGY"] = val
    #Les persos qui n'ont pas mangé au moins 1 poulet ne survivent pas. Cette option n'est pas fonctionnel car cela rend la simulation beaucoup moins bien
    """for pos in map:
        if map[pos]["objet"] in ["player_red","player_blue"]:
            if map[pos]["FOOD"] == 0:
                map[pos] = {"objet":"grass","IDENTIFIANT":"grass"+str(id(map[pos]))}
            else:
                map[pos]["FOOD"] = 0"""
    
def energy_compteur():
    """Supprime les personnages qui ont moins de 0 d'énergie"""
    mort = []
            
        #Tue ceux qui en ont moins de 0
        if map[pos]["objet"] in ["player_red","player_blue"] and map[pos]["ENERGY"] < 0:
            mort.append({pos:map[pos]["objet"]})
            map[pos] = {"objet":"grass","IDENTIFIANT":"grass"+str(id(map[pos]))}
    return mort


def hasard_camp():
    """Donne une position vide au hasard sur la map"""
    while True:
        hasard  = random.randint(0,largeur-1)
        hasard2 = random.randint(0,hauteur-1)
        if map[(hasard,hasard2)]["objet"] == "grass":
            #Camp sur un endroit aléatoire
            return (hasard,hasard2)

def reset_food():
    """Permet de réinitialiser le nombre de poulet mangé pour tous les personnages"""
    for i in map:
        if map[i] in ["player_blue","player_red"]:
            map[i]["FOOD"] = 0
