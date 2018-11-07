#! usr/bin/python3

def reverseString(sentence):
	return " ".join(sentence.split()[::-1])

def main():
	print(reverseString(input('Please enter a setence: ')))

if __name__ == '__main__':
	main()
