#! /usr/bin/python3

import random
import string

alphaUpper = string.ascii_uppercase # Weight: 20
alphaLower = string.ascii_lowercase # Weight: 20
digit = string.digits # Weight: 10
punctuation = '!@#$%.' # Weight: 5

# 0 - 20 is upper, 20 - 40 is lower, 40 - 50 is digits, 50 - 55 is punctuation
categoryKey = {'upper':20, 'lower':40, 'digit':50, 'punct':55}

def userInput():
	check = True
	while check==True:
		strength = input("Enter strength of password (weak, medium, strong): ")
		if strength.lower() in ('weak', 'medium', 'strong'):
			return strength.lower()
			check = False
		else:
			check = True
def charSelection():
	key = random.randrange(0, 55)
	if key < 20:
		#alphUpper
		return random.choice(alphaUpper)
	elif key >= 20 and key < 40:
		return random.choice(alphaLower)
	elif key >= 40 and key < 50:
		return random.choice(digit)
	elif key >= 50 and key <= 55:
		return random.choice(punctuation)
	
def passGeneration(stren):
	password = ''
	if stren = 'strong':
		# Need to add logic to generate random weight key to ensure more emphasis on alpha-numeric rather than puncuation
		for i in range(0, 15):
			password+=charSelection()
	elif stren = 'medium':
		# Need to add logic to generate random weight key to ensure more emphasis on alpha-numeric rather than puncuation
		for i in range(0, 8):
			password+=charSelection()
	else:
		# Need to add logic to generate random weight key to ensure more emphasis on alpha-numeric rather than puncuation
		for i in range(0, 6):
			password+=charSelection()
	return password

def main():
	passStrength = userInput()
	print(passGeneration(passStrength))

if __name__ == '__main__':
	main()
