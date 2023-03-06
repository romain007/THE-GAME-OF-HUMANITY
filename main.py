from Map.display import *
from Characters.move import *
from Data.data_managment import *
from Environment.case_occupe import *
import pygame
import sys
FPS = parametre["FPS"]
rules ={
        "player_red":
            {"attaque":"player_blue","param":["rock","player_red"]},
        "player_blue":
            {"attaque":"player_red","param":["rock","player_blue"]},
        "food":
            {"attaque":"False","param":["rock","player_red","player_blue","food"]}
       }

if __name__ == "__main__":

    # boucle d'événements
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        liste_id = {}
        #Liste de tous les players
        for position in statistique:
            if statistique[position]["objet"] in ["player_blue","player_red","food"] :
                liste_id[statistique[position]["IDENTIFIANT"]] = statistique[position]["objet"]
        dead = []
        historique = {}
        liste_id = melange_dico(liste_id)
        NO = []

        for identifiant,objet in liste_id.items():
            if identifiant in NO:
                continue
            h , i = move_perso(identifiant,rules[objet]["attaque"],rules[objet]["param"])
            historique.update(h)
            if i:
                NO.append(i)

        affichage(historique,temps=0.1)
        for i in dico.copy():
            del dico[i]
    # quitter pygame
    pygame.quit()
    sys.exit()
