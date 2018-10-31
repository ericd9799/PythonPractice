#! /usr/bin/python3

def main():
  str = ''
  word = input("Please enter word: ")
  
  for i in word:
    str = i + str
    
   if str == word:
    print("Palidrome -- string reversal")
   else:
    print("Not palidrome -- string reversal")
    
   if word == word[::-1]:
      print ("Palidrome -- word slicing")
   else:
      print ("Not palindrome -- word slicing")   
    

if(__name__) == '__main__':
  main()
