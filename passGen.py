#! /usr/bin/python3

import random
import string

alphaUpper = string.ascii_uppercase
alphaLower = string.ascii_lowercase
digit = string.digits
punctuation = string.punctuation

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
	print("Password strength: {}".format(passStrength))
	

if __name__ == '__main__':
	main()
