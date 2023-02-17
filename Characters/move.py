from Map.generation import *
import random
import pygame
#FICHIER POUR LE DEPLACEMENT DU PERSONNAGE

vect = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]] #liste toute les directions possibles


def move(vector, image,image2):
  """Le vector est sous la forme [x,y](exemple pour aller a droite c'est [1,0])"""
  position = [image.x,image.y]
  save = position[:]
  #Nouvelle position à partir du vecteur définis
  position[0] = position[0] - vector[1]
  position[1] = position[1] + vector[0]
  #Dans le cas ou on a une position sur une frontière, on réessaye des vecteurs aléatoire jusqu'a ne plus etre sur une frontière
  while position in limite :
    vector = random.choice(vect)
    position[0] = save[0] - vector[1]
    position[1] = save[1] + vector[0]

  #A partir des nouvelles position définis, on place le perso
  MAP[save[0] - vector[1]][save[1] + vector[0]] = image2
  image.x = save[0] - vector[1]
  image.y = save[1] + vector[0]
  #Dans le cas d'un vecteur [0,0] ou le personnage ne bougerait pas, il serait remplacé par rien, il disparaitrait donc de la map
  if vector != [0, 0]:
    #remplace l'encien endroit ou étais le perso par rien
    MAP[save[0]][save[1]] = grass_image
