#! /usr/bin/python3

def main():
  str = ''
  word = input("Please enter word: ")
  
  for i in word:
    str = i + str
    
   if str == word:
    print("Palidrome")
   else:
    print("Not palidrome")

if(__name__) == '__main__':
  main()
