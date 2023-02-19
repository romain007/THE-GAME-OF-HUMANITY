import colorama
import random
from Data.data_managment import *
import pygame
import json


#Récupére les paramètres
with open ("parametre.json","r",encoding="utf-8") as json_file:
  parametre = json.load(json_file)


statistique = {
"herbe":{},
"rock":{},
"perso_red":{},
"perso_blue":{},
"nourriture":{}
}
  
# Récupérer les informations de l'écran
pygame.init()
info = pygame.display.Info()

#Fait en sorte que tous s'adapte parfaitement à la taille de l'écran
diviseur = sorted(diviseurs_communs(info.current_w,info.current_h))
largeur = info.current_w//diviseur[parametre["ZOOM"]]
hauteur = info.current_h//diviseur[parametre["ZOOM"]]
print("ZOOM DE :",diviseur[parametre["ZOOM"]])

#load toutes les images avec les tailles voulues
size_largeur = diviseur[parametre["ZOOM"]]
size_hauteur = diviseur[parametre["ZOOM"]]

grass_image = pygame.image.load("sprite/grass.png")

player_image_blue = pygame.image.load("sprite/player.png")

player_image_red = pygame.image.load("sprite/player-red.png")

rock_image = pygame.image.load(r"sprite/rock.png")

food_image = pygame.image.load(r"sprite/food.png")

image={"grass_image":pygame.transform.scale(grass_image, (size_largeur,size_hauteur)),
"player_image_blue":pygame.transform.scale(player_image_blue, (size_largeur,size_hauteur)),
"player_image_red":pygame.transform.scale(player_image_red, (size_largeur,size_hauteur)),
"rock_image" : pygame.transform.scale(rock_image, (size_largeur,size_hauteur)),
"food_image" : pygame.transform.scale(food_image, (size_largeur,size_hauteur))
}

print(largeur,hauteur)
#Géneration de la matrice ainsi que tous ces élèments :
#Génération map vide
loop=0
for x in range(largeur):
  for y in range(hauteur):
    statistique["herbe"] = création_dico(statistique["herbe"],[f"herbe_{loop}","position"])
    statistique["herbe"][f"herbe_{loop}"]["position"] = [x,y]
    statistique["herbe"][f"herbe_{loop}"]["image"] = "grass_image"
    loop=loop+1

#Géneration de la limite
#PARTIE HAUTE
loop=0
for i in range(0,largeur):
  statistique["rock"] = création_dico(statistique["rock"],[f"rock_{loop}","position"])
  statistique["rock"][f"rock_{loop}"]["position"] = [i,0] 
  statistique["rock"][f"rock_{loop}"]["image"] = "rock_image"
  loop=loop+1
#PARTIE BASSE
for i in range(0,largeur):
  statistique["rock"] = création_dico(statistique["rock"],[f"rock_{loop}","position"])
  statistique["rock"][f"rock_{loop}"]["position"] = [i,hauteur-1]
  statistique["rock"][f"rock_{loop}"]["image"] = "rock_image"
  loop=loop+1
#PARTIE DROITE
for i in range(0,hauteur):
  statistique["rock"] = création_dico(statistique["rock"],[f"rock_{loop}","position"])
  statistique["rock"][f"rock_{loop}"]["position"] = [largeur-1,i]
  statistique["rock"][f"rock_{loop}"]["image"] = "rock_image"
  loop=loop+1
#PARTIE GAUCHE
for i in range(0,hauteur):
  statistique["rock"] = création_dico(statistique["rock"],[f"rock_{loop}","position"])
  statistique["rock"][f"rock_{loop}"]["position"] = [0,i]
  statistique["rock"][f"rock_{loop}"]["image"] = "rock_image"
  loop=loop+1

#Géneration de la nourriture à des endroits aléatoire
liste = []
for loop in range(parametre["NOMBRE NOURRITURE"]):
  hasard  = random.randint(1,largeur-2)
  hasard2 = random.randint(1,hauteur-2)
  while [hasard,hasard2] in liste:
    hasard  = random.randint(1,largeur-2)
    hasard2 = random.randint(1,hauteur-2)
  statistique["nourriture"] = création_dico(statistique["nourriture"],[f"poulet_{loop}","position"])
  statistique["nourriture"][f"poulet_{loop}"]["position"] = [hasard,hasard2]
  statistique["nourriture"][f"poulet_{loop}"]["image"] = "food_image"
  liste.append([hasard,hasard2])

#Génération des persos bleus
for loop in range(parametre["NOMBRE PERSO BLUE"]):
  #Pour un suivis de chaque personnage, ils ont chacun un identifiant unique
  statistique["perso_blue"] = création_dico(statistique["perso_blue"],[f"perso_blue{loop}","position"])
  statistique["perso_blue"][f"perso_blue{loop}"]["position"] = [random.randint(1,(largeur-2)),random.randint(1,(hauteur-2))]
  statistique["perso_blue"][f"perso_blue{loop}"]["image"] = "player_image_blue"

#Génération des persos rouge
for loop in range(parametre["NOMBRE PERSO RED"]):
  #Pour un suivis de chaque personnage, ils ont chacun un identifiant unique
  statistique["perso_red"] = création_dico(statistique["perso_red"],[f"perso_red{loop}","position"])
  statistique["perso_red"][f"perso_red{loop}"]["position"] = [random.randint(1,(largeur-2)),random.randint(1,(hauteur-2))]
  statistique["perso_red"][f"perso_red{loop}"]["image"] = "player_image_blue"

with open(r"Environment/statistique.json","w") as f:
  json.dump(statistique,f,indent=6)
