from Map.generation import *
from Data.data_managment import *
from Map.generation import *
import time
import pygame
import sys

screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))


def signe(a,b):
  if a<b:
    return -1
  if a>b:
    return 1
  else:
    return 0
    
#A partir de la matrice, affichage de tous les élèments avec pygame
def affichage(var=0):
  """lance pygame et affiche la matrice. Option d'écart entre chaque point matricielle et de décallage pour centrer la matrice"""
  global save
  
  ecart = diviseur[parametre["ZOOM"]]
  FPS = parametre["FPS"]

  historique={"food":{},"player_red":{},"player_blue":{}}
  
  for position in save:

      if save[position]["objet"] in historique:
        
        #OLD POSITION
        old_position = pygame.math.Vector2(position[0]*ecart,position[1]*ecart)

        #Teste si l'objet existe encore en le recherchant via son identifiant
        try:
          new = [(key[0]*ecart,key[1]*ecart) for key, value in statistique.items() if value['IDENTIFIANT'] == save[position]['IDENTIFIANT']][0]
        except:
          #old_position = pygame.math.Vector2(position[0]*ecart,position[1]*ecart)
          new = old_position

        #NEW POSITION
        new_position = pygame.math.Vector2(new[0],new[1])

        #Initialise historique
        historique[save[position]["objet"]][save[position]["IDENTIFIANT"]] = []
        
        i=0
        for loop in range(FPS):
          intermediate_pos = old_position.lerp(new_position, i/100)
          historique[save[position]["objet"]][save[position]["IDENTIFIANT"]].append(intermediate_pos)
          i=i+100/FPS
          
  screen.blit(background_surface, (0, 0))

  for loop in range(FPS):   
    
    for key in historique:
      for player in historique[key]:
        screen.blit(image[key],historique[key][player][loop])

    pygame.display.flip()
    time.sleep(var)

  save=statistique.copy()
  