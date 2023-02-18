from LEDADT import *
from ImageADT import *
from utime import sleep_ms

class LEDMatrix:
	def __init__(self, rowList, colList) -> None:
		self.RowPins = colList
		self.ColPins = rowList
		self.ROWS = [] 
		self.COLS = []
		self.Image = Image((5, 5))
		self.RowInterval = 100
		self.RefreshInterval = self.ROWS * self.RowInterval
		self.Init()

	def Init(self):
		self.ROWS = [] 
		self.COLS = []
		for pin in self.RowPins:
			self.ROWS += [LED(pin)]
		for pin in self.ColPins:
			self.COLS += [LED(pin)]

		self.TurnAllOff()

	def TurnAllOff(self): # Turns all LEDS OFF
		for led in self.ROWS:
			led.Off()
		for led in self.COLS:
			led.On()

	def LightSinglePixel(self, row, col):
		self.ROWS[col].On()
		self.COLS[row].Off()

	def RefreshImage(self):
		for row in range(self.Image.Rows):
			self.TurnAllOff()
			for col in range(self.Image.Columns):
				if self.Image.PixelIsOn(row, col):
					self.LightSinglePixel(row, col)
			sleep_ms(self.RowInterval)
		self.TurnAllOff()


