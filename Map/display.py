from Map.generation import *
from Data.data_managment import *
import time
import pygame
import sys


screen = pygame.display.set_mode((info_w, info_h))

def affichage(dico,temps=0):

    screen.blit(background_surface, (0, 0))
    for loop in range(FPS+1):   
        screen.blit(background_surface, (0, 0))
        for position in dico:
            screen.blit(image[position[1]],dico[position][loop])
            '''for i in mort:
                for key,value in i.items():
                    screen.blit(image[value],(key[0]*ecart,key[1]*ecart))'''
        time.sleep(temps)
        pygame.display.flip()

def val_inter(old_position,new_pos):

    #Définition des vecteurs initiaux et finaux. Les transforme en point a taille réel
    old_vector = pygame.math.Vector2(old_position[0]*ecart,old_position[1]*ecart)
    new_vector = pygame.math.Vector2(new_pos[0]*ecart,new_pos[1]*ecart)
    #Prend tous les coordonnés intermédiaire entre les 2 positions
    dico[str(old_position),statistique[old_position]["objet"]] = []

    #Remplissage d'un dictionnaire avec toute les valeurs intermédiaire
    i=0
    for loop in range(FPS+1):
        intermediate_vector = old_vector.lerp(new_vector, i/100)
        dico[str(old_position),statistique[old_position]["objet"]].append(intermediate_vector)
        i=i+100/FPS
