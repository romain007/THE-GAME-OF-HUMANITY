from Map.display import *
from Characters.move import *
from Data.data_managment import *
from Environment.case_occupe import *
from Environment.return_home import *
from Environment.gestion import *
from Map.statistique import *


FPS = parametre["FPS"]
TIME = parametre["TIME"]/100
save = 0
#Energie perdue ou gagné en fonction des actions :
parametre["ENERGY_MOVE"] = parametre["DAY"]/parametre["ENERGY_MOVE"] * -1 
parametre["ENERGY_FIGHT"] = parametre["DAY"]/parametre["ENERGY_FIGHT"] * -1 
parametre["ENERGY_LIFE"] = parametre["DAY"]/parametre["ENERGY_LIFE"] * -1 
parametre["ENERGY_FOOD"] = parametre["DAY"]/parametre["ENERGY_FOOD"]  *  1 
parametre["ENERGY_REPRODUCTION"] = parametre["DAY"]/parametre["ENERGY_REPRODUCTION"] * -1 

def game():
    global liste
    save = 0
    c = 0

    while True:
        c = c + 1   
        gamma_ = 0.85
        generate_poulet(parametre["NOMBRE NOURRITURE"]) #Genere nombre aléatoire de  poulets autour d'un nombre définis
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
                #gamma_ = gamma_ - 1/parametre["DAY"]
                pass

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

        compteur = 0
        z = 0
        #Permet de faire revenir tous les personnages chez eux. S'execute tant que tout le monde n'est pas rentré ou qu'un perso est coincer
        while compteur < len(liste_id):
            for identifiant,objet in liste_id.items():
                
                return_home(identifiant)
            
            affichage(mort=[],temps=TIME,gamma=gamma_,c=c)
            z = z + 1
            if z > 100:
                break
            #Ajoute au compteur et compare entre le nombre de perso sur leur maison et le nombre de perso totale
            compteur = 0
            for pos in map:
                if map[pos]["objet"] in ["player_blue","player_red"] and pos == map[pos]["CAMP"]:
                    compteur = compteur + 1

        restart() #Réinitialise l'energie pour tous les perso qui sont chez eux
        reset_camp()  #Remet à jour les camps en supprimant ceux des persos mort
        reset_food()

        d = 0
        for i in map:
            if map[i]["objet"] in ["player_red","player_blue"]:
                d = d + 1
        print("Nouveaux membres : ",d-save)

        liste = []
        save = d

        if c > parametre["DURE_JEU"]:
            break

    #Affiche log
    affiche_log()
    time.sleep(100)
    return

