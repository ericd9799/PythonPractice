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

def main():
	passStrength = userInput()
	password = ''
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
	print(password)

if __name__ == '__main__':
	main()
