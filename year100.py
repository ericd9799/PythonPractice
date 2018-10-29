#! /usr/bin/python3

import datetime

now = datetime.datetime.now()
year = now.year

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

yearsToHundred = 100 - age
turnHundred = int(year) + yearsToHundred

message = name + " will turn 100 in the year "+ str(turnHundred)

print(message)

repeat = int(input("Please enter integer to repeat message: "))

print(repeat * (message + "\n"))

