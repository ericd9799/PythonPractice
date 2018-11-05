#! /usr/bin/python3

import random

def main():

	guessCnt = 0
	genNum = random.randint(1, 9)
  
	while True:
		guess = int(input("Enter guess between 1 - 9: "))
		guessCnt += 1
	
		if guess < genNum:
			print ("Too low!")
			continue
		elif guess > genNum:
			print ("Too high!")
			continue
		elif guess == genNum:
			print ("Correct! You took "+ str(guessCnt) + " attempts!")
			if input("Enter Y to continue: ").upper() == "Y":
				continue
			else:
				break

if __name__ == "__main__":
	main()
