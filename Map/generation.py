import colorama
import random
from Data.data_managment import *
import pygame
#load toutes les images avec les tailles voulues
size_largeur = 50
size_hauteur = 50

grass_image = pygame.image.load("sprite\grass.png")
grass_image = pygame.transform.scale(grass_image, (size_largeur,size_hauteur))

player_image = pygame.image.load("sprite\player.png")
player_image = pygame.transform.scale(player_image, (size_largeur-2,size_hauteur))
player_rect = player_image.get_rect()

player2_image = pygame.image.load("sprite\player-red.png")
player2_image = pygame.transform.scale(player2_image, (size_largeur,size_hauteur))
player2_rect = player2_image.get_rect()

rock_image = pygame.image.load(r"sprite\rock.png")
rock_image = pygame.transform.scale(rock_image, (size_largeur,size_hauteur))

food_image = pygame.image.load(r"sprite\food.png")
food_image = pygame.transform.scale(food_image, (size_largeur,size_hauteur))


#Géneration de la matrice ainsi que tous ces élèments
largeur = int(lire(8,"parametre.txt"))
hauteur = int(lire(10,"parametre.txt"))



couleurs = {
  grass_image: colorama.Fore.WHITE,
  rock_image: colorama.Fore.BLUE,
  player_image: colorama.Fore.RED,
  player2_image : colorama.Fore.YELLOW,
  food_image: colorama.Fore.GREEN
}


#Génération
MAP = [[grass_image] * largeur for y in range(hauteur)]



def frontiere(front):
  liste = []
  #PARTIE HAUTE
  for i in range(0,largeur):
    MAP[0][i] = front
    liste.append([0,i])
  #PARTIE BASSE
  for i in range(0,largeur):
    MAP[hauteur-1][i] = front
    liste.append([hauteur-1,i])
  #PARTIE DROITE
  for i in range(0,hauteur):
    MAP[i][largeur-1] = front
    liste.append([i,largeur-1])
  #PARTIE GAUCHE
  for i in range(0,hauteur):
    MAP[i][0] = front
    liste.append([i,0])
  return liste

def bouffe(food,nb):
  liste=[]
  for i in range(nb):
    hasard  = random.randint(1,largeur-2)
    hasard2 = random.randint(1,hauteur-2)
    MAP[hasard2][hasard] = food
    if [hasard2,hasard] not in liste:
      liste.append([hasard2,hasard])
  return liste

limite = frontiere(rock_image)
nourriture = bouffe(food_image,int(lire(6,"parametre.txt")))

position = [random.randint(1,(hauteur-2)), random.randint(1,(largeur-2))]

MAP[position[0]][position[1]] = player_image
player_rect.x = position[0]
player_rect.y = position[1]

position2 = [random.randint(1,(hauteur-2)), random.randint(1,(largeur-2))]

MAP[position2[0]][position2[1]] = player2_image
player2_rect.x = position2[0]
player2_rect.y = position2[1]