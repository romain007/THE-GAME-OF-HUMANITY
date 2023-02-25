from Map.generation import *
from Data.data_managment import *
from Map.generation import *
import time
import pygame
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
  param=["food","player_red","player_blue"]


  historique={}
  
  for position in save:
      if save[position]["objet"] in param:
        old_position = position[0]*ecart,position[1]*ecart
        try:
          new_position = [(key[0]*ecart,key[1]*ecart) for key, value in statistique.items() if value['IDENTIFIANT'] == save[position]['IDENTIFIANT']][0]
        except:
          old_position = position[0]*ecart,position[1]*ecart
          new_position = old_position
        coordonnée = old_position
        historique[position] = []
        for loop in range(ecart):

          #Nouvelle coordonnée, entre old et new position
          coordonnée = (coordonnée[0]+1*signe(new_position[0],old_position[0]),coordonnée[1]+1*signe(new_position[1],old_position[1]))
                  
          historique[position].append(coordonnée)

  for loop in range(len(list(historique.values())[0])):
    screen.blit(background_surface, (0, 0))
    for key in historique:          

      screen.blit(image[save[key]["objet"]],historique[key][loop])

    pygame.display.flip()
    time.sleep(var)

  save=statistique.copy()

  


