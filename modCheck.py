#! /usr/bin/python3

modCheck = int(input("Please enter an integer: "))

if (modCheck % 4) == 0:
  print(str(modCheck) + " is a multiple of 4")
elif (modCheck % 2) == 0:
  print(str(modCheck) + " is even")
elif (modCheck % 2) != 0:
  print(str(modCheck) + " is odd")

num, check = input("Enter 2 numbers:").split()
num = int(num)
check = int(check)

if num % check == 0:
	print(str(check) + " divides evenly into " + str(num))
else:
	print(str(check) + " does not divide evenly into " + str(num))
