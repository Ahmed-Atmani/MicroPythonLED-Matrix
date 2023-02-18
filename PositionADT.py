class Position:
	def __init__(self, x=0, y=0) -> None:
		self.X = x
		self.Y = y
	
	def Move(self, direction, amount=1):
		match direction:
			case "up":
				self.Y -= amount
			case "down":
				self.Y += amount
			case "left":
				self.X -= amount
			case "right":
				self.X += amount
			case _:
				print("wrong direction (expected \"up\", \"down\, \"left\" or \"right\")")

	def __str__(self) -> str:
		return f"[{self.X} - {self.Y}]"