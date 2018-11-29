#! /usr/bin/python3

import random
import string

alphaUpper = string.ascii_uppercase
alphaLower = string.ascii_lowercase
digit = string.digits
punctuation = '!@#$%.'

def userInput():
	check = True
	while check==True:
		strength = input("Enter strength of password (weak, medium, strong): ")
		if strength.lower() in ('weak', 'medium', 'strong'):
			return strength.lower()
			check = False
		else:
			check = True
def passGeneration(stren):
	password = ''
	# Need to add logic to generate random weight key to ensure more emphasis on alpha-numeric rather than puncuation
	for i in range(0, 10):
		key = random.randrange(0, 4)
		if key == 0:
			#alphUpper
			password += random.choice(alphaUpper)
		elif key == 1:
			password += random.choice(alphaLower)
		elif key == 2:
			password += random.choice(digit)
		else:
			password += random.choice(punctuation)
	return password

def main():
	passStrength = userInput()
	print(passGeneration(passStrength))

if __name__ == '__main__':
	main()
