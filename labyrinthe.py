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

    def tryMove(self, robot, m, stepCount):
        row = robot[0]
        col = robot[1]

        if m.upper() == 'N':
            if row < stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row - i][col] == 'O':
                    return False

            robot = (row - stepCount, col)

        elif m.upper() == 'E':    
            if len(self.lab[row]) <= col + stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row][col + i] == 'O':
                    return False

            robot = (row, col + stepCount)

        elif m.upper() == 'S':
            if len(self.lab) <= row + stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row + i][col] == 'O':
                    return False

            robot = (row + stepCount, col)

        elif m.upper() == 'O':    
            if col < stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row][col - i] == 'O':
                    return False

            robot = (row, col - stepCount)

        else:
            return False

        return True

    def move(self, robot, m):
        step = 1
        if len(m) > 1:
            step = int(m[1:])
            m = m[:1]

        if not self.tryMove(m, step):
            print("Incorrect move !\n")

        if robot == self.exit:
            self.hasExited = True
        else:
            self.hasExited = False

    def isFree(self, i, j):
        if self.lab[i][j] != ' ' and self.lab[i][j] != 'U':
            return False
        for client, robot in self.robots.items():
            if i == robot[0] and j == robot[1]:
                return False

        return True

    def allFreeCase(self):
        cases = []
        for i in range(len(self.lab)):
            for j in range(len(self.lab[i])):
                if self.isFree(i,j):
                    cases.append((i,j))

        return cases