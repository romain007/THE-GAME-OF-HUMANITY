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
            if event.type == pygame.KEYDOWN:
                time.sleep(100)
        # déplacer le personnage vers un emplacement aléatoire
        move(random.choice(vect),player_rect,player_image)
        test_case_occupe(player_rect)
        move(random.choice(vect),player2_rect,player2_image)
        test_case_occupe(player2_rect)
        #mettre à jour l'affichage
        affichage_pygame(50)
        time.sleep(0.5)
        #affichage(position)



    # quitter pygame
    pygame.quit()
    sys.exit()













