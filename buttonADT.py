from machine import Pin

class Button:
	def __init__(self, gpioPin) -> None:
		self.gpioPin = gpioPin
		self.PIN = Pin(gpioPin, Pin.IN, Pin.PULL_UP)

	def Read(self):
		temp = self.PIN.value()
		if temp == 0:
			return True
		else:
			return False

