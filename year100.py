#! /usr/bin/python3

import datetime

now = datetime.datetime.now()
year = now.year
age = int(input("Please enter your age: "))

yearsToHundred = 100 - age
turnHundred = int(year) + yearsToHundred

print("You will turn 100 in the year "+ str(turnHundred))

