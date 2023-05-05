from Data.data_managment import *
from Environment.case_occupe import *
from Map.display import *
import time

#Ce module est composé des fonctions qui concernent la période de la nuit, quand les personnages rentrent chez eux

def rapprochement(depart,arrive):
    """Avec une position de départ, donne la prochaine case la plus proche"""
    if depart == arrive:
        return depart
    response,positions = filtre(next_to(depart),param=solid+["player_red","player_blue"])
    if not response:
        return depart
    dico = {}
    for pos in positions:
        dico[pos] = distance_euclidienne(pos,arrive)

    min_value = min(dico.values())
    min_keys = [key for key, value in dico.items() if value == min_value]

    chosen_key = random.choice(min_keys)
      
    return chosen_key


def return_home(identifiant):
    """Fais bouger un personnage à partir de son identifiant vers la case la plus proche de sa maison"""

    #Position actuelle de l'identifiant du perso

    old_position = [key for key, value in map.items() if value['IDENTIFIANT'] == identifiant][0]

    
    #Choisis la case la plus proche

    new_pos = rapprochement(old_position,map[old_position]["CAMP"])


    val = val_inter(old_position,new_pos)

    #Mise a jour des coordonées
    map[new_pos] = map[old_position].copy()
    map[new_pos]["MOVE"] = val

    if new_pos != old_position:
        map[old_position] = {"objet":"grass","IDENTIFIANT":"grass123"}

    return False
