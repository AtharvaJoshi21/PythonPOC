#WAP to accept a string from user and replace all occurrances of first character except for the first character.

def TransformString(inputStr, replaceToken):
	outputStr = inputStr[0] + inputStr[1:].replace(inputStr[0], replaceToken)
	return outputStr
	
inputString = input('Please enter a string: ')
replaceToken = input('Please enter a token to be replaced: ')
print ('String before transformation is : ', inputString)

print ('String after transformation is : ')
print (TransformString(inputString, replaceToken))