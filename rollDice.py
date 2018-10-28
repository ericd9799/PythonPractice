#! /usr/bin/python3

import random

roll = "Y"
while roll== "Y":
	print(random.randint(1, 6))
	roll = input("Continue? (Y/N)")
