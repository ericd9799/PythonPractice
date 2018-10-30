#! /usr/bin/python3

import random

def main():
	a = []
	b = []
	
	listSize =int(input("Enter size of list: "))
	compare = int(input("Enter integer to compare to: "))
	for x in range(listSize):
		a.insert(x, random.randrange(100))
	
	print("List a: "+str(a))
	
	for x in a:
		if x < compare:
			print(x)
			b.append(x)

	print("List b: "+str(b))
		


if(__name__) == '__main__':
	main()
