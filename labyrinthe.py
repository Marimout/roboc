# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""
    def __init__(self, labyrintheString):
        self.lab = labyrintheString.split('\n')
        self.hasExited = False

        # list of robots that are present in the labyrinth
        self.robots = []

        for i, line in enumerate(self.lab):
            for j in range(len(line)):
                if line[j] == 'U':
                    self.exit = (i,j)
                    break

    def __repr__(self, **kwargs):
        newLab = list(self.lab)

        for i in range(len(robots)):
            newLab[robot[0]] = newLab[robot[0]][:j] + str(i) + newLab[robot[0]][j+1:]

        rep = "\n".join(newLab)

        return rep

    def tryMove(self, m, stepCount):
        row = self.robot[0]
        col = self.robot[1]

        if m.upper() == 'N':
            if row < stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row - i][col] == 'O':
                    return False

            self.robot = (row - stepCount, col)

        elif m.upper() == 'E':    
            if len(self.lab[row]) <= col + stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row][col + i] == 'O':
                    return False

            self.robot = (row, col + stepCount)

        elif m.upper() == 'S':
            if len(self.lab) <= row + stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row + i][col] == 'O':
                    return False

            self.robot = (row + stepCount, col)

        elif m.upper() == 'O':    
            if col < stepCount:
                return False
            
            for i in range(stepCount+1):
                if self.lab[row][col - i] == 'O':
                    return False

            self.robot = (row, col - stepCount)

        else:
            return False

        return True

    def move(self, m):
        step = 1
        if len(m) > 1:
            step = int(m[1:])
            m = m[:1]

        if not self.tryMove(m, step):
            print("Incorrect move !\n")

        if self.robot == self.exit:
            self.hasExited = True
        else:
            self.hasExited = False

    def isFree(self, i, j):
        free = self.lab[i][j] == ' ' or self.lab[i][j] == 'U'
        for 