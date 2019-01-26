#WAP to accept a string from user and jumble the string such as:
#1. print odd indexed characters suffixed by even indexed characters
#2. print odd indexed characters suffixed by even indexed characters with reversed strings

def JumbleStrings(inputStr):
	outputStr = inputStr[0::2] + inputStr[1::2]
	return outputStr
	
def JumbleStringsRev(inputStr):
	outputStr = inputStr[::-2] + inputStr[-2::-2]
	return outputStr
	
inputString = input('Enter a string to be transformed: ')

print ('Jumbled Strings are: ')

print (JumbleStrings(inputString))
print (JumbleStringsRev(inputString))