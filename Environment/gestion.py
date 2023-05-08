from Map.generation import *
from Environment.case_occupe import *

#▶ Ce fichier est remplit de fonctions annexes, servant à la gestion de l'énergie, des camps, ect...

def kill(perso):
    """Entrée: perso
    Sortie: Null
    > Tue tous les personnages du type donné en entrée (player_red, player_blue, food, rock, grass...)
    en les remplaçant par de l'herbe."""
    for position in map:
        if map[position]["objet"] == perso:
            map[position] = {"objet":"grass","IDENTIFIANT":"grass123"}

            
            
def reset_camp():
    """Met à jour les campements (se déclanche lors d'un nouveau jour), fait apparaître les bébés
    dans leurs campements et supprime les campements attribués à des personnages morts."""
    #Liste des camps de tous les personnages

    liste_id = all_player(param=["player_red","player_blue"]) #Renvoie la liste de tout les player_red/player_blue en vie.

    #Fais apparaître les bébés.
    for perso in campement:
        if not campement[perso]["active"] and campement[perso]["parent"] in liste_id:
            campement[perso]["active"] = True  #On active le campement (permet de l'afficher)
            map[campement[perso]["position"] ]= campement[perso]["baby"]
            campement[perso]["baby"] = False

    liste_id = all_player(param=["player_red","player_blue"])

    #Supprime les campements.
    for perso in campement.copy():
        if perso not in liste_id:
            del campement[perso] #On supprime son campement

            
            
def restart(val=100):
    """> Remet à 100 d'énergie (énergie max) les personnages rentrés chez eux pour la nuit."""
    for pos in map:
        if map[pos]["objet"] in ["player_red","player_blue"] and pos == map[pos]["CAMP"]:
            map[pos]["ENERGY"] = val
            
    #Les personnages qui ne mangent pas de poulet ne survivent pas à la fin de la nuit.
    #Ce bout de code est supprimé car le nombre de personnages stagnait et rendait la simulation beaucoup moins bien.
    
    """for pos in map:
        if map[pos]["objet"] in ["player_red","player_blue"]:
            if map[pos]["FOOD"] == 0:
                map[pos] = {"objet":"grass","IDENTIFIANT":"grass"+str(id(map[pos]))}
            else:
                map[pos]["FOOD"] = 0"""
    
def energy_compteur():
    """> Tue tous les personnages qui ont 0 ou moins d'énergie et retourne les personnages qui sont mort (à cause de ça)."""
    mort = []
    for pos in map:            
        if map[pos]["objet"] in ["player_red","player_blue"] and map[pos]["ENERGY"] < 0:
            mort.append({pos:map[pos]["objet"]})
            map[pos] = {"objet":"grass","IDENTIFIANT":"grass"+str(id(map[pos]))}
    return mort



def hasard_camp():
    """> Donne une position vide au hasard sur la map pour pouvoir y placer un campement."""
    while True:
        hasard  = random.randint(0,largeur-1)
        hasard2 = random.randint(0,hauteur-1)
        if map[(hasard,hasard2)]["objet"] == "grass":
            #Camp sur un endroit aléatoire
            return (hasard,hasard2)

        
        
def reset_food():
    """Permet de réinitialiser le nombre de poulet mangé (la nourriture) pour tous les personnages."""
    for i in map:
        if map[i] in ["player_blue","player_red"]:
            map[i]["FOOD"] = 0
