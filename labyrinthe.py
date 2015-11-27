# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""
    def __init__(self, labyrintheString):
        self.lab = labyrintheString.split('\n')
        self.hasExited = False

        # list of robots that are present in the labyrinth
        self.robots = {}

        for i, line in enumerate(self.lab):
            for j in range(len(line)):
                if line[j] == 'U':
                    self.exit = (i,j)
                    break

    def __repr__(self, **kwargs):
        """Return a representation of the labyrinth with each robot represented by X"""
        newLab = list(self.lab)

        for clientInfo, robot in self.robots:
            newLab[robot[0]] = newLab[robot[0]][:robot[1]] + 'X' + newLab[robot[0]][robot[1]+1:]

        rep = "\n".join(newLab)

        return rep

    def reprWithOneMainRobot(self, robotKey):
        """Return a representation of the labyrinth with a main robot (X) and other robots (x)"""
        newLab = list(self.lab)

        for clientInfo, robot in self.robots.items():
            newLab[robot[0]] = newLab[robot[0]][:robot[1]] + 'x' + newLab[robot[0]][robot[1]+1:]

        r = self.robots[robotKey]
        newLab[r[0]] = newLab[r[0]][:r[1]] + 'X' + newLab[r[0]][r[1]+1:]

        rep = "\n".join(newLab)

        return rep

    def tryMove(self, robot, m):
        row = robot[0]
        col = robot[1]

        if m.upper() == 'N':
            if not self.isFree(row - 1, col):
                return None;            
            return (row - 1, col)
        elif m.upper() == 'E':    
            if not self.isFree(row, col + 1):
                return None
            return (row, col + 1)
        elif m.upper() == 'S':
            if not self.isFree(row + 1, col):
                return None
            return (row + 1, col)
        elif m.upper() == 'O':
            if not self.isFree(row, col - 1):
                return None
            return (row, col - 1)
        elif m[0].upper() == "P":
            # TODO : break the wall
            return None
        elif m[0].upper() == "M":
            # TODO : build the wall
            return None
        else:
            return None

        return None

    def move(self, robot, m):
        """ Move the robot and return the new position"""
        newRobot = self.tryMove(robot, m)
        if newRobot == None:
            print("Incorrect move !\n")
            return robot

        if newRobot == self.exit:
            self.hasExited = True
        else:
            self.hasExited = False
        
        return newRobot

    def isFree(self, i, j):
        """ Check if the case (i,j) is free (no obstacle, no other robot)"""
        if i < 0 or i > len(self.lab) or j < 0 or j > len(self.lab[0]):
            return False

        if self.lab[i][j] != ' ' and self.lab[i][j] != 'U':
            return False

        for client, robot in self.robots.items():
            if i == robot[0] and j == robot[1]:
                return False

        return True

    def allFreeCase(self):
        """ Return the list of all free cases of the labyrinth"""
        cases = []
        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if self.isFree(i,j):
                    cases.append((i,j))

        return cases