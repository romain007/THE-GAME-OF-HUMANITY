from Map.display import *
from Characters.move import *
from Data.data_managment import *
from Environment.case_occupe import *
import pygame
import sys
FPS = parametre["FPS"]
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
        screen.blit(background_surface, (0, 0))
        dico = {}
        liste= []
        mort = []
        #Liste de tous les players blue
        for position in statistique:
            if statistique[position]["objet"] == "player_blue":
                liste.append(statistique[position]["IDENTIFIANT"])
        #Pour chaque ancienne position
        for identifiant in liste:
            print(identifiant)
            try:
                old_position = [key for key, value in statistique.items() if value['IDENTIFIANT'] == identifiant][0]

                #Choisis une case au hasard
                new_pos = random.choice(next_to(old_position,param=["rock"]))
                print(f"POSITION : {old_position} -> NEW_POSITION : {new_pos}")

                #Définition des vecteurs initiaux et finaux. Les transforme en point a taille réel
                old_vector = pygame.math.Vector2(old_position[0]*ecart,old_position[1]*ecart)
                new_vector = pygame.math.Vector2(new_pos[0]*ecart,new_pos[1]*ecart)

                """if statistique[new_pos]['objet'] == "player_blue":
                    mort.append(new_pos)"""

                statistique[new_pos] = statistique[old_position].copy()
                statistique[old_position] = {"objet":"grass","IDENTIFIANT":random.randint(1,100000)}
                
                
                #Prend tous les coordonnés intermédiaire entre les 2 positions
                dico[str(old_position)] = []
                i=0
                #Remplissage d'un dictionnaire avec toute les valeurs intermédiaire
                for loop in range(FPS+1):
                    intermediate_vector = old_vector.lerp(new_vector, i/100)
                    dico[str(old_position)].append(intermediate_vector)
                    i=i+100/FPS
            except:
                pass

        for loop in range(FPS):   
            screen.blit(background_surface, (0, 0))
            for position in dico:
                screen.blit(image["player_blue"],dico[position][loop])
                """for dead in mort:
                    screen.blit(image["player_blue"],(dead[0]*ecart,dead[1]*ecart))"""
            pygame.display.flip()



        #move_all("player_blue",attaque="player_red",param=["rock"])
        
        #move_all("player_red",attaque="player_blue",param=["rock","player_red"])

        #move_pouleto(param=["player_red","rock","player_blue","food"])
        
        #mettre à jour l'affichage
        with open ("save.txt","w") as f:
            for i in statistique.items():
                f.write(str(i)+'\n')
        input()
    # quitter pygame
    pygame.quit()
    sys.exit()