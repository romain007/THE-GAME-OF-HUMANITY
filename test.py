from Map.generation import *
from Data.data_managment import *
from Map.generation import *
import time
import pygame




screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))



#A partir de la matrice, affichage de tous les élèments avec pygame
def affichage_pygame(var=0,):
  """lance pygame et affiche la matrice. Option d'écart entre chaque point matricielle et de décallage pour centrer la matrice"""
  global save
  #Met du vert en fond
  screen.fill((99,199,77))
  ecart = diviseur[parametre["ZOOM"]]
  param = ["food","player_red","player_blue"]  #objet qui bougent
  
  for position in save:
    if save[position]["objet"] in param:

      old_position = position  # (0,6)
      
      new_position = [key for key, value in statistique.items() if value['IDENTIFIANT'] == save[position]['IDENTIFIANT']][0] #(0,3456)

      coordonnée = old_position

      while coordonnée != new_position:

        print("coordonnée :",coordonnée,"Position :",new_position)

        screen.blit(image[save[position]["objet"]],(coordonnée[0]*ecart+mvt,coordonnée[1]*ecart+mvt))
        coordonnée = (coordonnée[0]/ecart+mvt, coordonnée[1]/ecart+mvt)

        pygame.display.update()
  save=statistique.copy()
  
  pygame.display.update()
  time.sleep(var)