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

	player1 = player(input("Enter name for player 1: "))
	player2 = player(input("Enter name for player 2: "))
	
	while True:
		player1.setChoice(input(player1.getName() + " enter (R)ock, (P)aper, (S)cissor: "))
		player2.setChoice(input(player2.getName() + " enter (R)ock, (P)aper, (S)cissor: "))
		#print(player1)
		#print(player2)
	
		if player1.getChoice() == player2.getChoice():
			print ("Tie!")
			
		elif player1.getChoice() == "R":
			if player2.getChoice() == "S":
				print(player1.getName() + " wins!")
				if input("Enter Y to play again: ") == "Y":
					continue
				else:
					print("Game over")
					break
			else:
				print(player2.getName() + " wins!")
				if input("Enter Y to play again: ") == "Y":
					continue
				else:
					print("Game over")
					break
		elif player1.getChoice() == "S":
			if player2.getChoice() == "P":
				print(player1.getName() + " wins!")
				if input("Enter Y to play again: ") == "Y":
					continue
				else:
					print("Game over")
					break
			else:
				print(player2.getName() + " wins!")
				if input("Enter Y to play again: ") == "Y":
					continue
				else:
					print("Game over")
					break
		elif player1.getChoice() == "P":
			if player2.getChoice() == "R":
				print(player1.getName() + " wins!")
				if input("Enter Y to play again: ") == "Y":
					continue
				else:
					print("Game over")
					break
			else:
				print(player2.getName() + " wins!")
				if input("Enter Y to play again: ") == "Y":
					continue
				else:
					print("Game over")
					break

if __name__ == "__main__":
	main()	
