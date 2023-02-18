from Map.generation import *
from Data.data_managment import *
from Map.generation import *
import time
import pygame
import colorama




screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
#Met du vert en fond
screen.fill((99,199,77))


#A partir de la matrice, affichage de tous les élèments avec pygame
def affichage_pygame(var=0,centrage=0):
  """lance pygame et affiche la matrice. Option d'écart entre chaque point matricielle et de décallage pour centrer la matrice"""
  ecart = diviseur[parametre["ZOOM"]]
  for key,value in statistique.items():
    for key,value2 in value.items():
      screen.blit(image[value2["image"]],(value2["position"][0]*ecart+centrage,value2["position"][1]*ecart+centrage))
  pygame.display.flip()
  time.sleep(var)
