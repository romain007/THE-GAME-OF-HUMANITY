from Map.generation import *
from Map.display import *
from Environment.case_occupe import *
from Environment.gestion import *
import random
import time



def fuite_perso(identifiant):
    old_position = [key for key, value in map.items() if value['IDENTIFIANT'] == identifiant][0]
    liste_pos = next_to(old_position)
    response,liste_pos = filtre(liste_pos.copy(),param=solid+["food","player_blue","player_red"])

    #Permet de ne pas bloquer le programme quand un perso a nulle part ou aller
    if not response:
        return False
    
    new_pos = random.choice(liste_pos)
    val = val_inter(old_position,new_pos)
    map[new_pos] = map[old_position].copy()
    map[new_pos]["MOVE"] = val
    map[old_position] = {"objet":"grass","IDENTIFIANT":"grass"+str(id(map[old_position]))}


def move(identifiant):
    mort = False

    #Position actuelle de l'identifiant du perso
    try:
        old_position = [key for key, value in map.items() if value['IDENTIFIANT'] == identifiant][0]
    except:
        #Perso est mort
        return False
    
    if map[old_position]["objet"] == "player_red":
        attaque = "player_blue"

    if map[old_position]["objet"] == "player_blue":
        attaque = "player_red"     

    #Liste des cases disponibles
    liste_pos = next_to(old_position)

    #Enleve les rochers et arbres
    response,liste_pos = filtre(liste_pos,param=solid)


    #Permet de ne pas bloquer le programme quand un perso a nulle part ou aller
    if not response:
        return False
 
    #Prend une position au hasard
    new_pos = random.choice(liste_pos)   


    response_attaque,liste_attaque = filtre_cible(liste_pos.copy(),param=[attaque])
    response_food,liste_food = filtre_cible(liste_pos.copy(),param=["food"])
    response_repr,liste_repr = filtre_cible(liste_pos.copy(),param=[map[old_position]["objet"]])

    #POWER
    #Si il y a un perso d'un clan opposé a coté de lui, il l'attaque
    if response_attaque:
        liste_pos = liste_attaque
        
        #Prend une position au hasard
        new_pos = random.choice(liste_pos)        


        map[old_position]["ENERGY"] = map[old_position]["ENERGY"] + parametre["ENERGY_FIGHT"]

        #L'attaquant est plus fort que que l'autre
        if map[old_position]["POWER"] > map[new_pos]["POWER"]:

            #L'attaqué prend la fuite
            rand_num = random.randint(0,100)
            if int(map[old_position]["SPEED"]/2) < rand_num: 

                new_pos = old_position
                fuite_perso(map[new_pos]["IDENTIFIANT"])
            #Prend pas la fuite
            else:

                mort = {new_pos:map[new_pos]["objet"]}
        #Moins fort que l'autre
        else:

            new_pos = old_position
        
        mise_a_jour(old_position,new_pos)
        return mort
    


    #Si il y a un poulet a coté de lui, il l'attaque
    elif response_food:
        liste_pos = liste_food
        
        new_pos = random.choice(liste_pos)
        rand_num = random.randint(0,100)
        #Si le poulet arrive à s'enfuir
        
        if map[old_position]["AGILITY"] < rand_num:
            fuite_perso(map[new_pos]["IDENTIFIANT"])
            map[old_position]["ENERGY"] =   map[old_position]["ENERGY"] + parametre["ENERGY_CATCH"]

        else:
            mort = {new_pos:map[new_pos]["objet"]}
            map[old_position]["ENERGY"] =   map[old_position]["ENERGY"] + parametre["ENERGY_FOOD"]
            map[old_position]["FOOD"] =   map[old_position]["FOOD"] + 1

        mise_a_jour(old_position,new_pos)
        return mort
    

    #REPRODUCTION
    elif response_repr :
        new_pos = random.choice(liste_repr)
        rand_num = random.randint(0,100)
        #Permet de faire en sorte que 2 persos ne se reproduisent plus ensemble
        if map[new_pos]["IDENTIFIANT"] not in map[old_position]["REPRODUCTION"] and map[old_position]["FERTILITE"] < rand_num and map[old_position]["FOOD"] > 1:
            map[new_pos]["ENERGY"] = map[new_pos]["ENERGY"] + parametre["ENERGY_REPRODUCTION"]
            map[old_position]["ENERGY"] = map[new_pos]["ENERGY"] + parametre["ENERGY_REPRODUCTION"]

            #FONT UN ENFANT
            rand_num = random.randint(1,2)

            #Permet de faire en sorte que 2 persos ne se reproduisent plus ensemble
            map[old_position]["REPRODUCTION"].append(map[new_pos]["IDENTIFIANT"])
            map[new_pos]["REPRODUCTION"].append(map[old_position]["IDENTIFIANT"])

            #Mutation génétiquemutation génétique aléatoire avec distribution gaussienne
            vitesse_enfant = (0.5 * map[old_position]["SPEED"]) + (0.5 * map[new_pos]["SPEED"])
            variance = 0.2 * vitesse_enfant
            mutation = random.gauss(0, variance)
            vitesse_enfant += mutation

            force_enfant = (0.5 * map[old_position]["POWER"]) + (0.5 * map[new_pos]["POWER"])
            variance = 0.2 * force_enfant
            mutation = random.gauss(0, variance)
            force_enfant += mutation

            agilité_enfant = (0.5 * map[old_position]["AGILITY"]) + (0.5 * map[new_pos]["AGILITY"])
            variance = 0.2 * agilité_enfant
            mutation = random.gauss(0, variance)
            agilité_enfant += mutation

            fertilité_enfant = (0.5 * map[old_position]["FERTILITE"]) + (0.5 * map[new_pos]["FERTILITE"])
            variance = 0.2 * fertilité_enfant
            mutation = random.gauss(0, variance)
            fertilité_enfant += mutation

            vitesse_enfant = (0.5 * map[old_position]["SPEED"]) + (0.5 * map[new_pos]["SPEED"])
            variance = 0.2 * vitesse_enfant
            mutation = random.gauss(0, variance)
            vitesse_enfant += mutation      

            var = random.random()

            #Prend une position de tente a coté de celle du parent en excluant
            position_campement = place_camp()

            #Création d'un nouveau campement pour l'enfant ainsi qu'un personnage    
            campement[f"{map[old_position]['objet']}{id(var)}"] = {"position":position_campement,
                                                                        "objet":map[old_position]["objet"],
                                                                        "baby":
                                                                                {"objet":map[old_position]["objet"],
                                                                                "IDENTIFIANT":f"{map[old_position]['objet']}{id(var)}",
                                                                                "SPEED":vitesse_enfant,
                                                                                "POWER":force_enfant,
                                                                                "AGILITY":agilité_enfant,
                                                                                "FERTILITE":fertilité_enfant,
                                                                                "FOOD":0,
                                                                                "ENERGY":100,
                                                                                "MOVE":val_inter(position_campement,position_campement),
                                                                                "CAMP":position_campement,
                                                                                "REPRODUCTION": [map[old_position]["IDENTIFIANT"],map[new_pos]["IDENTIFIANT"]]
                                                                            }}
            
            #Fais en sorte que les parents ne se reproduisent pas avec l'enfant AAAAAAA
            map[old_position]["REPRODUCTION"].append(f"{map[old_position]['objet']}{id(var)}")
            map[new_pos]["REPRODUCTION"].append(f"{map[old_position]['objet']}{id(var)}")

            new_pos = old_position
            mise_a_jour(old_position,new_pos)
            return mort
        
        #Si ils se dont deja reproduit ensemble, continue le programme
        else:
            response,liste_pos = filtre(next_to(old_position),param=solid+["player_red","player_blue"])
            if not response:
                return False
            new_pos = random.choice(liste_pos)



    #SPEED
    rand_num = random.randint(0,100)
    #Si ça variable speed est trop faible il bouge pas

    if map[old_position]["SPEED"] < rand_num and map[new_pos]["objet"] not in ["player_red","player_blue","food"]:
        new_pos = old_position
        mise_a_jour(old_position,new_pos)
        return mort



    mise_a_jour(old_position,new_pos)
    return mort

def move_pouleto(identifiant):
    mort = False

    #Position actuelle de l'identifiant du perso
    try:
        old_position = [key for key, value in map.items() if value['IDENTIFIANT'] == identifiant][0]
    except:
        #Perso est mort
        return False
    
    #Liste des cases disponibles
    liste_pos = next_to(old_position)
    response,liste_pos = filtre(liste_pos,param=solid+["player_red","player_blue","food"])

    #Permet de ne pas bloquer le programme quand un perso a nulle part ou aller
    if not response:
        return False

    #Prend une position au hasard
    new_pos = random.choice(liste_pos)    
    mise_a_jour(old_position,new_pos)
    return mort

def energy_compteur():
    mort = []
    for pos in map:
        if map[pos]["objet"] in ["player_red","player_blue"] and map[pos]["ENERGY"] > 100:
            map[pos]["ENERGY"] = 100

        if map[pos]["objet"] in ["player_red","player_blue"] and map[pos]["ENERGY"] < 0:
            mort.append({pos:map[pos]["objet"]})
            map[pos] = {"objet":"grass","IDENTIFIANT":"grass"+str(id(map[pos]))}
    return mort

def energy_restart(val=100):
    for pos in map:
        if map[pos]["objet"] in ["player_red","player_blue"] and pos == map[pos]["CAMP"]:
            map[pos]["ENERGY"] = val

def mise_a_jour(old_position,new_pos):
    #Mouvement entre 2 position (sert à l'animation)
    val = val_inter(old_position,new_pos)

    #Mise a jour des coordonées
    map[new_pos] = map[old_position].copy()
    map[new_pos]["MOVE"] = val

    #Si le perso a  bougé (evite que la case ou il se trouve se transforme en herbe)
    if new_pos != old_position:
        map[old_position] = {"objet":"grass","IDENTIFIANT":"grass"+str(id(map[old_position]))}
        map[new_pos]["ENERGY"] = map[new_pos]["ENERGY"] + parametre["ENERGY_MOVE"]