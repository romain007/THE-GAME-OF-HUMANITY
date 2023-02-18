from Map.generation import *
import random
import pygame
import sys
#FICHIER POUR LE DEPLACEMENT DU PERSONNAGE

vect = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]] #liste toute les directions possibles


def move_all():
  quitte = True
  s=0
  """Bouge tous les personnageLe vector est sous la forme [x,y](exemple pour aller a droite c'est [1,0])"""
  #Définis la liste de toutes les positions des cailloux existant
  liste_rock = []
  for key,value in statistique["rock"].items():
    liste_rock.append(value["position"])

  for key,perso in statistique["perso_blue"].items():
    s=s+1
    vector = random.choice(vect)
    #Place le perso à un endroit sans cailloux
    #while quitte:
    new_position = [perso["position"][0] + vector[0] ,perso["position"][1] -vector[1]]
    while quitte:
      print("NEW :",new_position)
      print("LISTE",liste_rock)
      if new_position in liste_rock:
        import sys
        sys.exit()
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        vector = random.choice(vect)
      else:
        quitte = False

    perso["position"] = new_position



        
def move(vector,position1,position2):
  """Prend en entré la position x et y d'un perso et renvoie une position x et y aléatoire sur un case à coté de la position initiale"""
  
  position = [position1,position2]
  save = position.copy()
  #Nouvelle position à partir du vecteur définis
  position[0] = position[0] - vector[1]
  position[1] = position[1] + vector[0]
  #Dans le cas ou on a une position sur une frontière, on réessaye des vecteurs aléatoire jusqu'a ne plus etre sur une frontière
  while position in limite :
    vector = random.choice(vect)
    position[0] = save[0] - vector[1]
    position[1] = save[1] + vector[0]

  #Retourne les coordonnées du nouveaux perso
  if save[0] - vector[1] == position1 and save[1] + vector[0] == position2:
    print("AAAAAAAAAAAAAAAAAAA")
  return (save[0] - vector[1],save[1] + vector[0])
