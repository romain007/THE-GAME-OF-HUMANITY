from Map.generation import *
import random
import pygame
import sys
#FICHIER POUR LE DEPLACEMENT DU PERSONNAGE

vect = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]] #liste toute les directions possibles


def move_all():
  """Bouge tous les personnageLe vector est sous la forme [x,y](exemple pour aller a droite c'est [1,0])"""
  #Définis la liste de toutes les positions des cailloux existant
  liste_rock = []
  for key,value in statistique["rock"].items():
    liste_rock.append(value["position"])

  for key,perso in statistique["perso_blue"].items():
    quitte = False

    vector = random.choice(vect)
    #Place le perso à un endroit sans cailloux
    while quitte == False:
      new_position = [perso["position"][0] + vector[0] ,perso["position"][1] -vector[1]]

      if new_position in liste_rock:
        vector = random.choice(vect)
      else:
        quitte = True
    #Met à jour position
    perso["position"] = new_position


