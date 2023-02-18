from ImageADT import *

def DisplayNumber(number, LedMatrix, digitDuration=5000):
	seconds = digitDuration # ms - time to show each digit
	interval = LedMatrix.RefreshInterval # ms - time per refresh
	duration = seconds // interval # amount of refreshes
	
	temp = str(number)

	while len(temp) != 0:
		LedMatrix.Image = numbersMatrices[int(temp[0])]
		for i in range(duration):
			LedMatrix.RefreshImage()

		temp = temp[1:]

numbersMatrices =  [
	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 1, 1, 0]]),

	Image(matrix=[[0, 1, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 1, 1, 1, 0]]),

	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 0, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[0, 1, 0, 0, 0],
	[0, 1, 1, 1, 0]]),

	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 0, 0, 1, 0],
	[0, 0, 1, 1, 0],
	[0, 0, 0, 1, 0],
	[0, 1, 1, 1, 0]]),

	Image(matrix=[[0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[0, 0, 0, 1, 0],
	[0, 0, 0, 1, 0]]),

	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 1, 0, 0, 0],
	[0, 1, 1, 1, 0],
	[0, 0, 0, 1, 0],
	[0, 1, 1, 1, 0]]),

	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 1, 0, 0, 0],
	[0, 1, 1, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 1, 1, 0]]),

	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 0, 0, 1, 0],
	[0, 0, 1, 0, 0],
	[0, 1, 0, 0, 0],
	[0, 1, 0, 0, 0]]),

	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 1, 1, 0]]),

	Image(matrix=[[0, 1, 1, 1, 0],
	[0, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[0, 0, 0, 1, 0],
	[0, 1, 1, 1, 0]])	]
