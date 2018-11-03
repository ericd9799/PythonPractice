myfile = open('test.txt')

print(myfile.read())

#Need to reset cursor to beginning before reading again
myfile.seek(0)

print(myfile.readlines()) #Grab list of content

myfile.seek(0)

#open file once and assign content to variable, no need to close file when using with open
with open('test.txt', mode = 'r') as myfile:
	contents = myfile.read()

print('with: ' + contents)


#appending to file
with open('test.txt', mode = 'a') as f:
	f.write('FOUR ON FOURTH')

with open('test.txt', mode = 'r') as f:
	print(f.read())

myfile.close()


