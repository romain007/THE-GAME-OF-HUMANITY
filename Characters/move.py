from Map.generation import *
import random

#FICHIER POUR LE DEPLACEMENT DU PERSONNAGE
vect = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]] #liste toute les directions possibles

def next_to(position):
    """renvoie la liste des 8 cases autour de la case d'entrée.Parametre : la liste des objet a exlure"""
    liste_objet={}
    for vector in vect:
        new_pos = (position[0] + vector[0],position[1] - vector[1])
        liste_objet[new_pos] = statistique[new_pos]

    return liste_objet

def move_all(caractère,attrap1="False",attrap2="False",param=[]):
  """Bouge tous les personnage Le vector est sous la forme [x,y](exemple pour aller a droite c'est [1,0])"""

  identifiant = []

  for position in statistique:
    if statistique[position]["objet"] == caractère and statistique[position]["IDENTIFIANT"] not in identifiant :
        #Aléatoire pour vitesse, agilité, ect
        
        
        #identifiant différentie chaque perso
        identifiant.append(statistique[position]["IDENTIFIANT"])
        cases = next_to(position)

        #Si il y a le premier objet qu'on veut attraper:
        for pos in cases:
          if cases[pos]["objet"] == attrap1:

            #Garde que les objets
            for pos in cases.copy():
              if cases[pos]["objet"] != attrap1:
                del cases[pos]
            break

        #Si il y a le deuxieme objet qu'on veut attraper:
        for pos in cases:
          if cases[pos]["objet"] == attrap2:

            #Garde que les objets
            for pos in cases.copy():
              if cases[pos]["objet"] != attrap2:
                del cases[pos]
            break

        #Garde que les cases sans les objets voulues
        for pos in cases.copy():
          if cases[pos]["objet"] in param:
            del cases[pos]
        #SPEEDWAGON
        rand_num = random.randint(0,100)
        if rand_num>statistique[position]["SPEED"]:
          cases={}
        #Dans le cas ou le perso peut pas bouger
        if cases == {}:
          cases={position:statistique[position]}

        hasard = random.choice(list(cases.items()))

        #Fais plus 1 a la variable du perso si mange poulet
        if hasard[1]["objet"] == "food" and ( statistique[position]["objet"] == "player_blue" or statistique[position]["objet"] == "player_red") :
          rand_num = random.randint(0,100)
          if rand_num<=statistique[position]["AGILITY"] :
            statistique[position]["FOOD"] = statistique[position]["FOOD"]+1
          else:
            fuite_pouleto(hasard[1]["IDENTIFIANT"],["food","player_blue","player_red","rock"])
        
        #Se bat si autre perso
        if ( hasard[1]["objet"] == "player_red"or hasard[1]["objet"] == "player_blue") and ( statistique[position]["objet"] == "player_blue" or statistique[position]["objet"] == "player_red") :
          rand_num = random.randint(0,100)
          if rand_num>statistique[position]["POWER"] :
            print(statistique[position]["POWER"])
            hasard = (position,"CLAIRE")

        print(hasard[0])
        new_position = hasard[0]

        
        #Met à jour position 
        statistique[new_position] = statistique[position]
        if position != new_position:
          #Met à jour l'ancienne position
          statistique[position] = {"objet":"grass","IDENTIFIANT":random.randint(0,10000000)}

      

def fuite_pouleto(id,param=[]):
  for position in statistique:

    if statistique[position]["objet"] == "food" and statistique[position]["IDENTIFIANT"] == id:

      cases = next_to(position)
      #Garde que les cases sans les objets voulues
      for pos in cases.copy():
        if cases[pos]["objet"] in param:
          del cases[pos]
      if cases == {}:
        cases={position:'prout'}
      new_position = random.choice(list(cases.keys()))
      statistique[new_position] = statistique[position]
      break


