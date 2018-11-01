#! /usr/bin/python3

def main():
	string  = ""
	string2 = ""
	word = input("Please enter word: ")

	for x in word:
		string = x + string
	
	if string == word:
		print(word+" is a palindrome -- for loop reversal")
	else:
		print(word+" is not a palindrome -- for loop reversal")

	string2 = word[::-1]

	if string2 == word:
		print(word+" is a palindrome -- string slicing")
	else:
		print(word+" is not a palindrome -- string slicing")
    

if(__name__) == '__main__':
	main()
