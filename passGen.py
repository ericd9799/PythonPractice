#! /usr/bin/python3

import random
import string

alphaUpper = string.ascii_uppercase # Weight: 20
alphaLower = string.ascii_lowercase # Weight: 20
digit = string.digits # Weight: 10
punctuation = '!@#$%.' # Weight: 5

upperDict = dict(zip(range(0,26), string.ascii_uppercase))
lowerDict = dict(zip(range(0,26), string.ascii_lowercase))
digitDict = dict(zip(range(0,10), string.digits))
punctDict = {0:'!', 1:'@', 2:'#', 3:'$', 4:'%', 5:'.'}

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
	key = random.randrange(0, 40)
	if key < 15:
		#alphUpper
		return upperDict[key]
	elif key >= 15 and key < 30:
		return lowerDict[key]
	elif key >= 30 and key < 35:
		return digitDict[key]
	elif key >= 35 and key <= 40:
		return punctDict[key]
	
def passGeneration(stren):
	password = ''
	if stren == 'strong':
		# Need to add logic to generate random weight key to ensure more emphasis on alpha-numeric rather than puncuation
		for i in range(0, 10):
			password+=charSelection()
	elif stren == 'medium':
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
