#WAP to accept a string from user and print first two and last two characters.

def FuncSubStr(inputStr):
	outputStr = inputStr[:2]+inputStr[-2:]
	return outputStr

inputString = input('Enter a string : ')

if len(inputString) <= 2:
	print ('Invalid string')
else:
	print (FuncSubStr(inputString))