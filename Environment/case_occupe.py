from Map.generation import *

#Condition dans l'environnement
def test_case_occupe():
    poper=[]
    #Pour chaque perso
    for key,perso in statistique["perso_blue"].items():
        for key2,food in statistique["nourriture"].items():
            if perso["position"] == food["position"]:
                poper.append(key2)
    for i in poper:
        statistique["nourriture"].pop(i)


