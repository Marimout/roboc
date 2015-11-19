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
if not game:
	map = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
	map = int(map) - 1
	game = Game(cartes[map].nom, cartes[map].labyrinthe)

while True:
	print(game.labyrinthe)
	m = input("Enter a move : ")
	exit = game.labyrinthe.move(m)
	if exit:
		print("Félicitation ! Vous avez gagné !")
		break

