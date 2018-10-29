#! /usr/bin/python

import random

sysGenNum = random.randint(0, 10)

guess = int(input("Input guess (between 0 and 10): "))

while guess !=  sysGenNum:
	if guess > sysGenNum:
		print("Guess is too high")
		guess = int(input("Input guess (between 0 and 10): "))
	elif guess < sysGenNum:
		print("Guess is too low")
		guess = int(input("Input guess (between 0 and 10): "))



if guess == sysGenNum:
	print("You are correct!")
