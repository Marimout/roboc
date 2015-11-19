# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""
	def __init__(self, labyrintheString):
		self.lab = labyrintheString.split('\n')

		for i, line in enumerate(self.lab):
			for j in range(len(line)):
				if line[j] == 'X':
					self.robot = (i,j)
					self.lab[i] = line[:j] + ' ' + line[j+1:]
					break
				elif line[j] == 'U':
					self.exit = (i,j)
					break

	def __repr__(self, **kwargs):
		rep = ""
		for i, line in enumerate(self.lab):
			if i == self.robot[0]:
				j = self.robot[1]
				s = line[:j] + 'X' + line[j+1:]
			else:
				s = line
			rep += s + '\n'

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

		return True

	def move(self, m):
		step = 1
		if len(m) > 1:
			step = int(m[1:])
			m = m[:1]

		if not self.tryMove(m, step):
			print("Incorrect move !")

		if self.robot == self.exit:
			return True
		else:
			return False

