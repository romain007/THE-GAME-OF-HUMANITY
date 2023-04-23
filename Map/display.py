from Map.generation import *
from Data.data_managment import *
import time
import pygame
import sys

#Fait par ROMAIN

screen = pygame.display.set_mode((info_w, info_h))

def en_fonction_var(objet):
    if objet["objet"] == "food":
        return "food"
    liste = [objet['SPEED'],objet['POWER'],objet['AGILITY'],objet["FERTILITE"]]
    
    
    if liste[0] == max(liste):
        return objet["objet"]+"_speed"
    if liste[1] == max(liste):
        return objet["objet"]+"_power"
    if liste[2] == max(liste):
        return objet["objet"]+"_agility"
    if liste[3] == max(liste):
        return objet["objet"]+"_fertile"


def affichage(mort,temps=0,gamma=0.5,c=0):


    pygame.display.set_gamma(gamma)
    font = pygame.font.Font(None, int(parametre["ZOOM"]*2))
    font2 = pygame.font.Font(None, 40)

    # créer une surface pour le rectangle blanc
    rect_surface = pygame.Surface((350, 50))
    rect_surface.fill((255, 255, 255))
    # créer une surface pour le texte
    text_surface = font2.render(f'NOMBRE DE JOUR : {c}', True, (0, 0, 0))
    rect_surface.blit(text_surface,(10,10))
    screen.blit(background_surface, (0, 0))


    
    for loop in range(FPS+1):
        # dessiner le texte sur la surface du rectangle
   
        screen.blit(background_surface, (0, 0))
        

        for identifiant in campement:

            screen.blit(image2[campement[identifiant]["objet"]],(campement[identifiant]["position"][0]*ecart,campement[identifiant]["position"][1]*ecart))  #Maison perso

        for i in mort:
            for key,value in i.items():
                screen.blit(image3[value],(key[0]*ecart,key[1]*ecart))

        for position in map:
            if map[position]["objet"] in ["player_blue","player_red","food"]:

                screen.blit(image[en_fonction_var(map[position])],map[position]["MOVE"][loop])  #Perso
                if map[position]["objet"] not in ["food"]:
                    text_surface = font.render(f"{map[position]['ENERGY']}/100", True, (255 , 255 ,255))
                    screen.blit(text_surface, (map[position]["MOVE"][loop][0],map[position]["MOVE"][loop][1]-26))  #Barre de vie


        screen.blit(rect_surface, (largeur,hauteur))

        time.sleep(temps)
        pygame.display.flip()


def val_inter(old_position,new_pos):
    #Définition des vecteurs initiaux et finaux. Les transforme en point a taille réel
    old_vector = pygame.math.Vector2(old_position[0]*ecart,old_position[1]*ecart)
    new_vector = pygame.math.Vector2(new_pos[0]*ecart,new_pos[1]*ecart)
    #Prend tous les coordonnés intermédiaire entre les 2 positions
    liste = []

    #Remplissage d'un dictionnaire avec toute les valeurs intermédiaire
    i=0
    for loop in range(FPS+1):
        intermediate_vector = old_vector.lerp(new_vector, i/100)
        liste.append(intermediate_vector)
        i=i+100/FPS
    return liste
