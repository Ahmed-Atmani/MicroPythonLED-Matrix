from machine import ADC

class Accelerometer:
	def __init__(self, xyzPins=[26, 27, 28]) -> None:
		self.X = ADC(xyzPins[0])
		self.Y = ADC(xyzPins[1])
		self.Z = ADC(xyzPins[2])
	
	def ReadAxis(self, axis):
		result = int(((axis.read_u16() - 26000)/130)*2) - 6
		if result > 200:
			return 100
		elif result < 0:
			return -100
		else:
			return result - 100

	def ReadX(self):
		return - self.ReadAxis(self.X)
	
	def ReadY(self):
		return self.ReadAxis(self.Y)

	def ReadZ(self):
		return self.ReadAxis(self.Z)
