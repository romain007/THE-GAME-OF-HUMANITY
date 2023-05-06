import random
from Data.data_managment import *
import pygame
import json


#Fait par ROBIN


#Récupére les paramètres
with open ("parametre.json","r",encoding="utf-8") as json_file:
  parametre = json.load(json_file)
FPS = parametre["FPS"]

map = {}
campement = {}
stat = []

# Récupérer les informations de l'écran
pygame.init()
info = pygame.display.Info()
info_w = info.current_w
info_h = info.current_h
background_surface = pygame.Surface((info_w,info_h))

background_surface.fill((99,199,77))


#Fait en sorte que tous s'adapte parfaitement à la taille de l'écran
diviseur = sorted(diviseurs_communs(info_w,info_h))
largeur = info_w//diviseur[parametre["ZOOM"]]
hauteur = info_h//diviseur[parametre["ZOOM"]]
print("ZOOM DE :",diviseur[parametre["ZOOM"]])

#load toutes les images avec les tailles voulues
size_largeur = diviseur[parametre["ZOOM"]]
size_hauteur = diviseur[parametre["ZOOM"]]
ecart = diviseur[parametre["ZOOM"]]

image ={
  "grass":pygame.transform.scale(pygame.image.load("sprite/grass.png"),(size_largeur,size_hauteur)),
  "player_blue_speed":pygame.transform.scale(pygame.image.load("sprite/player_blue_speed.png"),(size_largeur,size_hauteur)),
  "player_blue_power":pygame.transform.scale(pygame.image.load("sprite/player_blue_power.png"),(size_largeur,size_hauteur)),
  "player_blue_agility":pygame.transform.scale(pygame.image.load("sprite/player_blue_agility.png"),(size_largeur,size_hauteur)),
  "player_blue_fertile":pygame.transform.scale(pygame.image.load("sprite/player_blue_fertile.png"),(size_largeur,size_hauteur)),
  "player_red_power":pygame.transform.scale(pygame.image.load("sprite/player_red_power.png"),(size_largeur,size_hauteur)),
  "player_red_agility":pygame.transform.scale(pygame.image.load("sprite/player_red_agility.png"),(size_largeur,size_hauteur)),
  "player_red_speed":pygame.transform.scale(pygame.image.load("sprite/player_red_speed.png"),(size_largeur,size_hauteur)),
  "player_red_fertile":pygame.transform.scale(pygame.image.load("sprite/player_red_fertile.png"),(size_largeur,size_hauteur)),
  "rock":pygame.transform.scale(pygame.image.load("sprite/rock.png"),(size_largeur,size_hauteur)),
  "food":pygame.transform.scale(pygame.image.load("sprite/food.png"),(size_largeur,size_hauteur)),
  "tree":pygame.transform.scale(pygame.image.load("sprite/tree.png"),(size_largeur,size_hauteur)),
  "tent_blue":pygame.transform.scale(pygame.image.load("sprite/blue_tent.png"),(size_largeur,size_hauteur)),
  "tent_red":pygame.transform.scale(pygame.image.load("sprite/red_tent.png"),(size_largeur,size_hauteur))
}
image2 = {  #Sert pour les campements
   "player_blue":pygame.transform.scale(pygame.image.load("sprite/blue_tent.png"),(size_largeur,size_hauteur)),
   "player_red":pygame.transform.scale(pygame.image.load("sprite/red_tent.png"),(size_largeur,size_hauteur)),

}
image3 = {
   "player_blue":pygame.transform.scale(pygame.image.load("sprite/player_blue_death.png"),(size_largeur,size_hauteur)),
   "player_red":pygame.transform.scale(pygame.image.load("sprite/player_red_death.png"),(size_largeur,size_hauteur)),
   "food":pygame.transform.scale(pygame.image.load("sprite/chicken_death.png"),(size_largeur,size_hauteur))
}

print(largeur*hauteur)
#Géneration de la matrice ainsi que tous ces élèments :
#Génération map vide
loop=0
for x in range(largeur):
  for y in range(hauteur):
    map[(x,y)] = {"objet":"grass","IDENTIFIANT":f"grass{loop}"}
    background_surface.blit(image["grass"],(x*ecart,y*ecart))
    loop=loop+1

#Géneration cailloux sur la bordure et à des endroits aléatoire
loop = 0
for i in range(largeur):
    for j in range(hauteur):
        if i == 0 or j == 0 or i == largeur-1 or j == hauteur-1:
            map[(i, j)]["objet"] = "rock"
            map[(i, j)]["IDENTIFIANT"] = f"rock{loop}"
            background_surface.blit(image["rock"],(i*ecart,j*ecart))
            loop = loop+1


positions_cailloux = [(random.randint(0, largeur-1), random.randint(0, hauteur-1)) for i in range(parametre["CAILLOUX"])]
positions_arbres = [(random.randint(0, largeur-1), random.randint(0, hauteur-1)) for i in range(parametre["ARBRE"])]

#CHAT GPT-------------------------------------------------------------------------------------------------------------
def regrouper(positions, seuil_min, seuil_max):
    groupes = []
    while positions:
        groupe = [positions.pop()]
        for pos in positions[:]:
            distances = [abs(pos[0]-p[0]) + abs(pos[1]-p[1]) for p in groupe]
            moyenne = sum(distances) / len(distances)
            seuil = min(seuil_max, max(seuil_min, moyenne))
            if any(d <= seuil for d in distances):
                groupe.append(pos)
                positions.remove(pos)
        groupes.append(groupe)
    return groupes

seuil_cailloux_min = parametre["CAILLOUX"]/2
seuil_cailloux_max = parametre["CAILLOUX"]
seuil_arbres_min = parametre["ARBRE"]/2
seuil_arbres_max = parametre["ARBRE"]

groupes_cailloux = regrouper(positions_cailloux, seuil_cailloux_min,seuil_cailloux_max)
groupes_arbres = regrouper(positions_arbres, seuil_arbres_min,seuil_arbres_max)
#CHAT GPT-------------------------------------------------------------------------------------------------------------

# Placer les groupes de cailloux et d'arbres sur la matrice
for groupe in groupes_cailloux:
    for pos in groupe:
        if map[pos]["objet"] == "grass":
          map[pos]["objet"] = "rock"
          map[pos]["IDENTIFIANT"] = f"rock{random.randint(1,1000000)}"
          background_surface.blit(image["rock"],(pos[0]*ecart,pos[1]*ecart))

loop = 0
for groupe in groupes_arbres:
    for pos in groupe:
        if map[pos]["objet"] == "grass":
          map[pos]["objet"] = "tree"
          map[pos]["IDENTIFIANT"] = f"tree{loop}"
          background_surface.blit(image["tree"],(pos[0]*ecart,pos[1]*ecart))
          loop = loop + 1

def generate_poulet(x):
  #Géneration de la nourriture à des endroits aléatoire
  loop=0
  while loop < x:
    hasard  = random.randint(0,largeur-1)
    hasard2 = random.randint(0,hauteur-1)
    if map[(hasard,hasard2)]["objet"] == "grass" :
      map[(hasard,hasard2)]["objet"] = "food"
      map[(hasard,hasard2)]["IDENTIFIANT"] = f"food{random.randint(0,10000000000000)}"
      map[(hasard,hasard2)]["SPEED"] = 50
      map[(hasard,hasard2)]["AGILITY"] = 0
      map[(hasard,hasard2)]["VECTOR"] = 0
      map[(hasard,hasard2)]["MOVE"] = []
      map[(hasard,hasard2)]["ENERGY"] = 100000000
      loop=loop+1

#Génération des persos bleus ainsi que de toutes leurs variables
loop=0
while loop < parametre["NOMBRE PERSO BLUE"]:
  #Pour un suivis de chaque personnage, ils ont chacun un identifiant unique
  hasard  = random.randint(0,largeur-1)
  hasard2 = random.randint(0,hauteur-1)
  if map[(hasard,hasard2)]["objet"] == "grass":
    map[(hasard,hasard2)]["objet"] = "player_blue"
    map[(hasard,hasard2)]["FOOD"] = 0
    map[(hasard,hasard2)]["SPEED"] = random.randint(0,100)
    map[(hasard,hasard2)]["AGILITY"] = random.randint(0,100)
    map[(hasard,hasard2)]["POWER"] = random.randint(0,100)
    map[(hasard,hasard2)]["FERTILITE"] = random.randint(0,100)
    map[(hasard,hasard2)]["ENERGY"] = 100
    map[(hasard,hasard2)]["IDENTIFIANT"] = f"player_blue{loop}"
    map[(hasard,hasard2)]["MOVE"] = []
    map[(hasard,hasard2)]["CAMP"] = (hasard,hasard2)
    map[(hasard,hasard2)]["REPRODUCTION"] = []
    #map[(hasard,hasard2)]["BABY"] = []
    campement[f"player_blue{loop}"] = {"position":(hasard,hasard2),"objet":"player_blue","baby":False,"active":True,"parent":"player_blue"}
    loop=loop+1

#Génération des persos rouges ainsi que de toutes leurs variables
loop=0
while loop < parametre["NOMBRE PERSO RED"]:
  #Pour un suivis de chaque personnage, ils ont chacun un identifiant unique
  hasard  = random.randint(0,largeur-1)
  hasard2 = random.randint(0,hauteur-1)
  if map[(hasard,hasard2)]["objet"] == "grass":
    map[(hasard,hasard2)]["objet"] = "player_red"
    map[(hasard,hasard2)]["FOOD"] = 0
    map[(hasard,hasard2)]["SPEED"] = random.randint(0,100)
    map[(hasard,hasard2)]["AGILITY"] = random.randint(0,100)
    map[(hasard,hasard2)]["POWER"] = random.randint(0,100)
    map[(hasard,hasard2)]["FERTILITE"] = random.randint(0,100)
    map[(hasard,hasard2)]["ENERGY"] = 100
    map[(hasard,hasard2)]["IDENTIFIANT"] = f"player_red{loop}"
    map[(hasard,hasard2)]["MOVE"] = []
    map[(hasard,hasard2)]["CAMP"] = (hasard,hasard2)
    map[(hasard,hasard2)]["REPRODUCTION"] = []
    #map[(hasard,hasard2)]["BABY"] = []
    campement[f"player_red{loop}"] = {"position":(hasard,hasard2),"objet":"player_red","baby":False,"active":True,"parent":"player_red"}
    loop=loop+1

solid = ["rock","tree"]
