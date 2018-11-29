#! /usr/bin/python3

import random
import string

alphaUpper = string.ascii_uppercase # Weight: 20
alphaLower = string.ascii_lowercase # Weight: 20
digit = string.digits # Weight: 10
punctuation = '!@#$%.' # Weight: 5

# 0 - 20 is upper, 20 - 40 is lower, 40 - 50 is digits, 50 - 55 is punctuation
categoryKey = {20:'upper', 40:'lower', 50:'digit', 55:'punct'}

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
