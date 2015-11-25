# -*-coding:Utf-8 -*

import os
import pickle

from carte import Carte
from game import Game

def selectMap():
    """Ask user to select a map and return it"""

    # Load all map from "cartes" folder
    cartes = []
    for filename in os.listdir("cartes"):
        if filename.endswith(".txt"):
            path = os.path.join("cartes", filename)
            mapName = filename[:-3].lower()
            with open(path, "r") as mapFile:
                mapContent = mapFile.read()
                cartes.append(Carte(mapName, mapContent))

    # Display all existing maps
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))


    # Ask user to select a map
    while True:
        try:
            map = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
            map = int(map) - 1
            if map < 0 or map >= len(cartes):
                raise ValueError
            break
        except ValueError:
            print("Numéro de labyrinthe incorrect ! Merci de resaisir !")

    return cartes[map]
