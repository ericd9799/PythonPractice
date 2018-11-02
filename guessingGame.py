#! /usr/bin/python3

import random

def main():
  genNum = random.randint(1, 9)
  guessCnt = 0
  correct = "N"
  
  while correct != "Y":
    guess = int(input("Please enter a guess between 1 - 9: "))
    guessCnt = guessCnt + 1
  
    if guess > genNum:
      print("Your guess is too high")
      correct = "N"
    elif guess < genNum:
      print("Your guess is too low")
      correct = "N"
    elif guess == genNum:
      print("You are correct! You took "+ str(guessCnt) + " guess(es).")
      correct = "Y"
  
  if correct = "Y":
     if input("Please enter Y to play again: ") == "Y":
        main()
     else:
        break
  
 if __name__ = "__main__":
    main()
