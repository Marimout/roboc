# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import pickle

from carte import Carte
from game import Game

# On charge les cartes existantes
cartes = []
for filename in os.listdir("cartes"):
    if filename.endswith(".txt"):
        path = os.path.join("cartes", filename)
        mapName = filename[:-3].lower()
        with open(path, "r") as mapFile:
            mapContent = mapFile.read()
            cartes.append(Carte(mapName, mapContent))

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

try:
    with open("savedgame.txt", "rb") as savedFile:
        unpickler = pickle.Unpickler(savedFile)
        game = unpickler.load()
except:
    game = None

# if there isn't any saved game then ask user to choose a map then init the game
if (not game) or (game.labyrinthe.hasExited):
    while True:
        try:
            map = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
            map = int(map) - 1
            if map < 0 or map >= len(cartes):
                raise ValueError
            break
        except ValueError:
            print("Numéro de labyrinthe incorrect ! Merci de resaisir !")
                
    game = Game(cartes[map].nom, cartes[map].labyrinthe)
    print("On commence : carte {0}".format(game.mapName))
else:
    print("On reprend le jeu précédent : carte {0}".format(game.mapName))

while True:
    print(game.labyrinthe)
    m = input("Enter a move : ")

    game.labyrinthe.move(m)

    # dump the game after each move
    with open("savedgame.txt", "wb") as savedFile:
        pickler = pickle.Pickler(savedFile)
        pickler.dump(game)

    if game.labyrinthe.hasExited:
        print("Félicitation ! Vous avez gagné !")
        break

    if m.upper() == 'Q':
        print("Au revoir ! A bientôt !")
        break

