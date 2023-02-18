from PositionADT import Position


class Image:
	def __init__(self, dimensions=None, matrix=None) -> None:

		# If matrix is given
		if matrix != None:
			self.Matrix = matrix
			self.Rows = len(matrix)
			self.Columns = len(matrix[0])

		# If dimensions are given
		elif dimensions != None:
			self.Rows = dimensions[0]
			self.Columns = dimensions[1]
			self.Matrix =  [[0 for x in range(self.Columns)] for y in range(self.Rows)]

		# Nothing is given
		else:
			self.Matrix = self.Columns = self.Rows = None
	
	def GetPixel(self, row, col):
		return self.Matrix[row][col]

	def SetPixel(self, row, col, val):
		self.Matrix[row][col] = val

	def TurnOnPixel(self, position):
		self.SetPixel(position.Y, position.X, 1)
	
	def TurnOffPixel(self, position):
		self.SetPixel(position.Y, position.X, 0)
	
	def PixelIsOn(self, row, col):
		return self.Matrix[row][col] == 1

	def PrintMatrix(self):
		for row in self.Matrix:
			print(row)