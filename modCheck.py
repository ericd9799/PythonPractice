#! /usr/bin/python3

modCheck = int(input("Please enter an integer: "))

if (modCheck % 4) == 0:
  print(str(modCheck) + " is a multiple of 4")
elif (modCheck % 2) == 0:
  print(str(modCheck) + " is even")
elif (modCheck % 2) != 0:
  print(str(modCheck) + " is odd")

num = int(input("Enter 2 numbers:"))
print ("Num: "+num+", Check: "+check)
