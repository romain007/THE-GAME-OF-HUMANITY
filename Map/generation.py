import random
from Data.data_managment import *
import pygame
import json


#Récupére les paramètres
with open ("parametre.json","r",encoding="utf-8") as json_file:
  parametre = json.load(json_file)


statistique = {}
  
# Récupérer les informations de l'écran
pygame.init()
info = pygame.display.Info()

background_surface = pygame.Surface((info.current_w,info.current_h))
background_surface.fill((99,199,77))

#Fait en sorte que tous s'adapte parfaitement à la taille de l'écran
diviseur = sorted(diviseurs_communs(info.current_w,info.current_h))
largeur = info.current_w//diviseur[parametre["ZOOM"]]
hauteur = info.current_h//diviseur[parametre["ZOOM"]]
print("ZOOM DE :",diviseur[parametre["ZOOM"]])

#load toutes les images avec les tailles voulues
size_largeur = diviseur[parametre["ZOOM"]]
size_hauteur = diviseur[parametre["ZOOM"]]
ecart = diviseur[parametre["ZOOM"]]

image ={
  "grass":pygame.transform.scale(pygame.image.load("sprite/grass.png"),(size_largeur,size_hauteur)),
  "player_blue":pygame.transform.scale(pygame.image.load("sprite/player.png"),(size_largeur,size_hauteur)),
  "player_red":pygame.transform.scale(pygame.image.load("sprite/player-red.png"),(size_largeur,size_hauteur)),
  "rock":pygame.transform.scale(pygame.image.load("sprite/rock.png"),(size_largeur,size_hauteur)),
  "food":pygame.transform.scale(pygame.image.load("sprite/food.png"),(size_largeur,size_hauteur))
}

print(largeur*hauteur)
#Géneration de la matrice ainsi que tous ces élèments :
#Génération map vide
loop=0
for x in range(largeur):
  for y in range(hauteur):
    statistique[(x,y)] = {"objet":"grass","IDENTIFIANT":f"grass{loop}"}
    background_surface.blit(image["grass"],(x*ecart,y*ecart))
    loop=loop+1

loop = 0
for i in range(largeur):
    for j in range(hauteur):
        if i == 0 or j == 0 or i == largeur-1 or j == hauteur-1:
            statistique[(i, j)]["objet"] = "rock"
            statistique[(i, j)]["IDENTIFIANT"] = f"rock{loop}"
            background_surface.blit(image["rock"],(i*ecart,j*ecart))
            loop = loop+1


#Géneration de la nourriture à des endroits aléatoire
loop=0
while loop < parametre["NOMBRE NOURRITURE"]:
  hasard  = random.randint(0,largeur-1)
  hasard2 = random.randint(0,hauteur-1)
  if statistique[(hasard,hasard2)]["objet"] == "grass" :
    statistique[(hasard,hasard2)]["objet"] = "food"
    statistique[(hasard,hasard2)]["IDENTIFIANT"] = f"food{loop}"
    statistique[(hasard,hasard2)]["SPEED"] = 50
    loop=loop+1

#Génération des persos bleus
loop=0
while loop < parametre["NOMBRE PERSO BLUE"]:
  #Pour un suivis de chaque personnage, ils ont chacun un identifiant unique
  hasard  = random.randint(0,largeur-1)
  hasard2 = random.randint(0,hauteur-1)
  if statistique[(hasard,hasard2)]["objet"] == "grass":
    statistique[(hasard,hasard2)]["objet"] = "player_blue"
    statistique[(hasard,hasard2)]["FOOD"] = 0
    statistique[(hasard,hasard2)]["SPEED"] = random.randint(90,100)
    statistique[(hasard,hasard2)]["AGILITY"] = random.randint(0,100)
    statistique[(hasard,hasard2)]["POWER"] = random.randint(0,100)
    statistique[(hasard,hasard2)]["SMART"] = 0
    statistique[(hasard,hasard2)]["IDENTIFIANT"] = f"player_blue{loop}"
    loop=loop+1

#Génération des persos rouges
loop=0
while loop < parametre["NOMBRE PERSO RED"]:
  #Pour un suivis de chaque personnage, ils ont chacun un identifiant unique
  hasard  = random.randint(0,largeur-1)
  hasard2 = random.randint(0,hauteur-1)
  if statistique[(hasard,hasard2)]["objet"] == "grass":
    statistique[(hasard,hasard2)]["objet"] = "player_red"
    statistique[(hasard,hasard2)]["FOOD"] = 0
    statistique[(hasard,hasard2)]["SPEED"] = random.randint(90,100)
    statistique[(hasard,hasard2)]["AGILITY"] = random.randint(0,100)
    statistique[(hasard,hasard2)]["POWER"] = random.randint(0,100)
    statistique[(hasard,hasard2)]["SMART"] = 0
    statistique[(hasard,hasard2)]["IDENTIFIANT"] = f"player_red{loop}"
    loop=loop+1


save = statistique.copy()  
