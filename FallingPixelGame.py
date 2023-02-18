from tkinter import Checkbutton
from LEDADT import LED
from buttonADT import Button
from LEDMatrixADT import LEDMatrix
from ImageADT import Image
from NumbersImages import *
from PositionADT import Position
from utime import sleep

class FallingPixelGame:
	def __init__(self, LEDMatrix, LeftButton, RightButton) -> None:
		self.LedMatrix = LEDMatrix
		self.LeftButton = LeftButton
		self.RightButton = RightButton

		self.Paddle = Position(self.LedMatrix.ROWS - 1, 2)
		self.Pixel = Position(-1, -1)
		self.Score = 0
		self.Lives = 3
	
	def CheckButtons(self):
		left = self.LeftButton.Read()
		right = self.RightButton.Read()

		if left and not right:
			self.Paddle.Move("left")
		elif right and not left:
			self.Paddle.Move("right")

	def LetPixelFall(self):
		self.Pixel.Move("down")

	def UpdateFrame(self):
		temp = Image(dimensions=(self.LedMatrix.COLS, self.LedMatrix.ROWS))
		temp.TurnOnPixel(self.Pixel)
		temp.TurnOnPixel(self.Paddle)

		


	def GameLoop(self):
		# user input
		self.CheckButtons()

		# move pixel
		self.LetPixelFall()

		# check collision

		# display frame
		self.UpdateFrame()


	def ShowScore(self):
		DisplayNumber(self.Score, self.LedMatrix)