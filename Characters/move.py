from Map.generation import *
from Map.display import *
from Environment.case_occupe import *
import random
import time



def fuite_pouleto(identifiant):
    old_position = [key for key, value in statistique.items() if value['IDENTIFIANT'] == identifiant][0]
    new_pos = random.choice(next_to(old_position,attaque='False',param=["player_blue","player_red","food","rock"]))
    val_inter(old_position,new_pos)
    statistique[new_pos] = statistique[old_position]
    statistique[old_position] = {"objet":"grass","IDENTIFIANT":"grass1234"}
    return  statistique[new_pos]["IDENTIFIANT"]

def init_pos():
    for position in statistique:
        if statistique[position]["objet"] == "player_blue" or statistique[position]["objet"] == "player_red" or statistique[position]["objet"] == "food" :
            statistique[position]["MOVE"] = False

def move_perso(identifiant,attaque='False',param=[]):

    mort = []
    ident = False
    #Position actuelle de l'identifiant du perso

    old_position = [key for key, value in statistique.items() if value['IDENTIFIANT'] == identifiant][0]


    #Choisis une case au hasard
    new_pos = random.choice(next_to(old_position,attaque,param=param))

    #SPEED
    rand_num = random.randint(0,100)
    #Si ça variable speed est trop faible il bouge pas
    if statistique[old_position]["SPEED"] < rand_num and statistique[new_pos]["objet"] not in ["player_red","player_blue","food"]:
        new_pos = old_position
    
    #AGILITY
    rand_num = random.randint(0,100)
    #Si ça variable agility est trop faible il attrape pas le pouleto
    if statistique[old_position]["AGILITY"] < rand_num and statistique[new_pos]["objet"] == "food" and statistique[old_position]["objet"] in ["player_red","player_blue"]:
        ident = fuite_pouleto(statistique[new_pos]["IDENTIFIANT"])
    
    #AGILITY
    rand_num = random.randint(0,100)
    #Si ça variable trop faible il tue pas l'autre
    if statistique[old_position]["POWER"] < rand_num and statistique[new_pos]["objet"] == attaque and statistique[old_position]["objet"] in ["player_red","player_blue"]:
        new_pos = old_position

    val_inter(old_position,new_pos)

    if statistique[new_pos]["objet"] == attaque or statistique[new_pos]["objet"] == "food": #and statistique[new_pos]["MOVE"] == False:
        ident = statistique[new_pos]["IDENTIFIANT"]

    #Mise a jour des coordonées
    statistique[new_pos] = statistique[old_position].copy()
    if new_pos != old_position:
        statistique[old_position] = {"objet":"grass","IDENTIFIANT":"grass123"}

    return dico , ident