from Map.display import *
from Characters.move import *
from Data.data_managment import *
from Environment.case_occupe import *
import pygame
import sys
clock = pygame.time.Clock()

FPS = diviseur[parametre["FPS"]]

if __name__ == "__main__":

    # boucle d'événements
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.KEYDOWN:
                #time.sleep(100)
        



        VAR = random.randint(0,1)
        # déplacer le personnage vers un emplacement aléatoire
        if VAR == 1:
            move_all("player_blue",attrap1="player_red",attrap2="food",param=["rock","player_blue"])
            move_all("player_red",attrap1="player_blue",attrap2="food",param=["rock","player_red"])
        if VAR == 0:
            move_all("player_red",attrap1="player_blue",attrap2="food",param=["rock","player_red"])
            move_all("player_blue",attrap1="player_red",attrap2="food",param=["rock","player_blue"])
        move_all("food",param=["player_red","rock","player_blue","food"])
        
        #mettre à jour l'affichage
        affichage(0.009)
        clock.tick(FPS)


    # quitter pygame
    pygame.quit()
    sys.exit()













