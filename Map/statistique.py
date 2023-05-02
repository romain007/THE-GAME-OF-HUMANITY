from Map.generation import *
import matplotlib.pyplot as plt

def update_log():
    statistique = {"speed":[],"power":[],"agility":[],"fertilite":[],"nb_perso":0,"nourriture_mange":[],"color_red":0,"color_blue":0}
    try:
        for i in map:
            if map[i]["objet"] in ["player_red","player_blue"]:
                statistique["speed"].append(map[i]["SPEED"])
                statistique["power"].append(map[i]["POWER"])
                statistique["agility"].append(map[i]["AGILITY"])
                statistique["fertilite"].append(map[i]["FERTILITE"])
                statistique["nourriture_mange"].append(map[i]["FOOD"])
                statistique["nb_perso"] = statistique["nb_perso"] + 1
                if map[i]["objet"] == "player_red":
                    statistique["color_red"] = statistique["color_red"] + 1
                if map[i]["objet"] == "player_blue":
                    statistique["color_blue"] = statistique["color_blue"] + 1
        statistique["speed"] = sum(statistique["speed"])/len(statistique["speed"])      
        statistique["power"] = sum(statistique["power"])/len(statistique["power"])   
        statistique["agility"] = sum(statistique["agility"])/len(statistique["agility"])   
        statistique["fertilite"] = sum(statistique["fertilite"])/len(statistique["fertilite"])   
        statistique["nourriture_mange"] = sum(statistique["nourriture_mange"])/len(statistique["nourriture_mange"])   

        stat.append(statistique)
    except:
        pass

def affiche_log():


    # initialiser les listes pour stocker les données à tracer
    speed_data = [d["speed"] for d in stat]
    power_data = [d["power"] for d in stat]
    agility_data = [d["agility"] for d in stat]
    fertilite_data = [d["fertilite"] for d in stat]
    nb_perso_data = [d["nb_perso"] for d in stat]
    nourriture_data = [d["nourriture_mange"] for d in stat]
    red_data = [d["color_red"] for d in stat]
    blue_data = [d["color_blue"] for d in stat]


    x_values = []

    # extraire les données de la liste de dictionnaires
    for i, d in enumerate(stat):
        x_values.append(i)

    # tracer les courbes de vitesse et de puissance en fonction de l'indice de la liste
    plt.plot(x_values, speed_data, label='vitesse')
    plt.plot(x_values, power_data, label='puissance')
    plt.plot(x_values, agility_data, label='agilité')
    plt.plot(x_values, fertilite_data, label='fertilité')
    plt.plot(x_values, nb_perso_data, label='population')
    plt.plot(x_values, nourriture_data, label='nourriture_mangé')
    plt.plot(x_values, red_data, label='population-rouge')
    plt.plot(x_values, blue_data, label='population-bleu')

    # ajouter des légendes et un titre
    plt.legend()
    plt.title("Evolution des différentes variables au cour du temps")

    # afficher le graphique
    plt.show()
