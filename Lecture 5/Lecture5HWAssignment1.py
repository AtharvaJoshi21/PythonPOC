#WAP to accept a string from user and print first two and last two characters.

inputStr = input('Enter a string : ')

if len(inputStr) <= 2:
	print ('Invalid string')

print (inputStr[:2]+inputStr[-2:])