#! /usr/bin/python3

import random

def listOverlap(a, b):
	both = [ itemOne for itemOne in set(a) for itemTwo in b if itemOne == itemTwo]
	# not necessary to perform inner for-loop to iterate through list
	# could have used in-clause since it is list
	return both

def listOverlapGenerate():
	a = [random.sample(random.randint(1, 10),12)]
	b = [random.sample(random.randint(1, 10), 10)]
	
	result = [itemOne for itemOne in set(a) if itemOne in b]
	return result

def main():
	print(listOverlap([1,1,2,3,5,6,7,8],[1,2,3,4,5,6,7,8]))
	print(listOverlapGenerate())

if __name__ == "__main__":
	main()