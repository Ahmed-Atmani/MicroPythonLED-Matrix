from machine import Pin

class LED:
	def __init__(self, gpioPin) -> None:
		self.State = False
		self.gpioPin = gpioPin
		self.PIN = Pin(gpioPin, Pin.OUT)
		self.Off()
	
	def On(self):
		self.PIN.value(1)
		self.State = True

	def Off(self):
		self.PIN.value(0)
		self.State = False

	def Toggle(self):
		if self.State:
			self.Off()
		else:
			self.On()

