#! /usr/bin/python3

def listOverlap(a, b):
	both = [ itemOne for itemOne in set(a) for itemTwo in b if itemOne == itemTwo]
	# not necessary to perform inner for-loop to iterate through list
	# could have used in-clause since it is list
	return both

def main():
	print(listOverlap([1,1,2,3,5,6,7,8],[1,2,3,4,5,6,7,8]))

if __name__ == "__main__":
	main()
