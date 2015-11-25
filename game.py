# -*-coding:Utf-8 -*

"""
Ce module contient la classe Game.
Un game = 1 nom de carte + 1 Labyrinthe
"""

class Game:

    """Classe représentant un labyrinthe."""
    def __init__(self, mapName, labyrinthe):
        self.mapName = mapName
        self.labyrinthe = labyrinthe

    def __repr__(self, **kwargs):
        return "<Game on {0}>".format(self.mapName)

