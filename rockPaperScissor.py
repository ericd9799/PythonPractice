#! /usr/bin/python3

class player():
	def __init__(self, name):
		self.name = name
	
	def options(self, opt):
		self.option = opt

	def __str__(self):
		return self.name + " selected "+ self.option
def main():
	player1 = player(input("Enter name for player 1: "))
	player2 = player(input("Enter name for player 2: "))
	player1.options(input("Enter (R)ock, (P)aper, (S)cissor: "))
	print(player1)

if __name__ == "__main__":
	main()
