from Map.display import *
from Characters.move import *
from Data.data_managment import *
from Environment.case_occupe import *
from Environment.return_home import *
from Environment.gestion import *
from Map.statistique import *


FPS = parametre["FPS"]
TIME = parametre["TIME"]/10



def game():

    c = 0

    while True:
        c = c + 1   
        gamma_ = 0.85
        generate_poulet()

        #Un jour complet
        for tour in range(parametre["DAY"]):

            liste_id = all_player(param=["food","player_blue","player_red"])

            #Melange dictionnaire pour que chaque perso joue chacun leur tour aléatoirement
            liste_id = melange_dico(liste_id)

            #Liste des players mort pour les afficher à l'écran
            liste_mort = []

            for identifiant,objet in liste_id.items():

                if objet == "food":
                    mort = move_pouleto(identifiant)

                else:

                    mort = move(identifiant)

                if mort:
                    liste_mort.append(mort)

                    

            #Mise à jour de l'affichage
            if tour >= parametre["DAY"]/2:
                gamma_ = gamma_ - 1/parametre["DAY"]

            liste_mort = liste_mort + energy_compteur() #Supprime les persos qui n'ont plus assez d'energie

            affichage(mort = liste_mort,temps=TIME,gamma=gamma_,c=c)

            '''with open("map.txt","w",encoding="utf-8") as f:
                for i,value in map.items():
                    f.write(str(i) + "" + str(value))
                    f.write("\n")'''

        #RETURN HOME
        kill("food")
        #Met a jour les logs
        update_log()
        liste_id = all_player(param=["player_red","player_blue"])

        for loop in range(parametre["DAY_RETURN_HOME"]):
            for identifiant,objet in liste_id.items():
                
                return_home(identifiant)
            
            affichage(mort=[],temps=TIME,gamma=gamma_,c=c)


            #Finit la boucle si tout le monde est rentré chez soi
            compteur = 0
            for pos in map:
                if map[pos]["objet"] in ["player_blue","player_red"] and pos == map[pos]["CAMP"]:
                    compteur = compteur + 1
            
            if compteur == len(liste_id):
                break

        camp()  #Remet à jour les camps en supprimant ceux des persos mort
        energy_restart() #Réinitialise l'energie pour tous les perso qui sont chez eux
        reset_food()

        if c > parametre["DURE_JEU"]:
            break

    #Affiche log
    affiche_log()
    time.sleep(100)
    return

