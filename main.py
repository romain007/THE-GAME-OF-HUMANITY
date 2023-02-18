import random
import copy
from Map.display import *
from Characters.move import *
from Data.data_managment import *
from Environment.case_occupe import *
import pygame
import sys
import random

if __name__ == "__main__":
    
    # boucle d'événements
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.KEYDOWN:
                #time.sleep(100)
        affichage_pygame(0.1)
        # déplacer le personnage vers un emplacement aléatoire
        move_all()
        #move_all(player_image_red)
        test_case_occupe()
        #mettre à jour l'affichage


    # quitter pygame
    pygame.quit()
    sys.exit()













