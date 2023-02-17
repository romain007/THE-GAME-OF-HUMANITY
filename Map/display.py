from Map.generation import MAP
from Data.data_managment import *
from Map.generation import *
import time
import pygame
import colorama

pygame.init()

# obtenir la taille de la résolution de l'écran
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((99,199,77))

#Affichage de la matrice (sert pas à grand chose)
def affichage(pos, var=0):
  time.sleep(var)
  for element in MAP:
    for element2 in element:
      print(couleurs[element2] + str(element2), end="")
    print('')
  print(colorama.Fore.RESET)

#A partir de la matrice, affichage de tous les élèments avec pygame
def affichage_pygame(ecart,centrage=0):
  """lance pygame et affiche la matrice. Option d'écart entre chaque point matricielle et de décallage pour centrer la matrice"""
  for x in range(largeur):
    for y in range(hauteur):
      screen.blit(MAP[y][x],(x*ecart+centrage,y*ecart+centrage))
  pygame.display.flip()

