#! /usr/bin/python3

def main():
	string  = ""
	string2 = ""
	word = input("Please enter word: ")

	# reverse word using for-loop
	for x in word:
		string = x + string

	if string == word:
		print(word+" is a palindrome -- for loop reversal")
	else:
		print(word+" is not a palindrome -- for loop reversal")

	# reverse string using step in slicing
	string2 = word[::-1]

	if string2 == word:
		print(word+" is a palindrome -- string slicing")
	else:
		print(word+" is not a palindrome -- string slicing")

	'''comment within atom'''

if(__name__) == '__main__':
	main()
