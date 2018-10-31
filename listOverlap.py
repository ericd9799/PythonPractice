#! /usr/bin/python3

import random

def main():
	listA = [1, 2, 3]
	listB = [4, 5, 1]
	listC = []
	sizeA, sizeB = input('Please enter two list lengths: ').split()
	sizeA = int(sizeA)
	sizeB = int(sizeB)

	for x in range(0, sizeA):
		listA.append(random.randrange(0, 100))

	print(listA)

	for y in range(0, sizeB):
		listB.append(random.randrange(0, 100))

	print(listB)

	for x in range(len(listA)):
		for y in range(len(listB)):
			if listA[x] == listB[y]:
				listC.append(listA[x])

	print(listC)

if __name__ == '__main__':
	main()
