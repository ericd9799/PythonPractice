#! /usr/bin/python3

class player():
	choice = ""
	def __init__(self, name):
		self.name = name	
	
	def setChoice(self, choice):
		'''Need to work on error handling'''
		#if choice in ["R", "P", "S"]:
		self.choice = choice
		#else:
			#print(choice + " is not a valid option.")
			#self.choice = print (self.name + " enter (R)ock, (P)aper, (S)cissor: ")

	def __str__(self):
		return self.name + " selected "+self.choice

	def getName(self):
		return self.name

	def getChoice(self):
		return self.choice
def main():
	won = "N"
	player1 = player(input("Enter name for player 1: "))
	player2 = player(input("Enter name for player 2: "))
	
	while won != "Y" and again = != "N":
		player1.setChoice(input(player1.getName() + " enter (R)ock, (P)aper, (S)cissor: "))
		player2.setChoice(input(player2.getName() + " enter (R)ock, (P)aper, (S)cissor: "))
		#print(player1)
		#print(player2)
	
		if player1.getChoice() == player2.getChoice():
			print ("Tie!")
			won = "N"
		elif player1.getChoice() == "R":
			if player2.getChoice() == "S":
				print(player1.getName() + " wins!")
				won = "Y"
			else:
				print(player2.getName() + " wins!")
				won = "Y"
		elif player1.getChoice() == "S":
			if player2.getChoice() == "P":
				print(player1.getName() + " wins!")
				won = "Y"
			else:
				print(player2.getName() + " wins!")
				won = "Y"
		elif player1.getChoice() == "P":
			if player2.getChoice() == "R":
				print(player1.getName() + " wins!")
				won = "Y"
			else:
				print(player2.getName() + " wins!")
				won = "Y"
		again = input("Enter Y to play again")
	'''When someone has won, ask if want to restart.
	Using recursive call of main() method to restart game.'''
	'''if won == "Y":
		again = input("Enter Y to play again: ")
		if again == "Y":
			main()
		else: 
			sys.exit()'''	

if __name__ == "__main__":
	main()
	
