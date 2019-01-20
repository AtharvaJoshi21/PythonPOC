#WAP to accept a string from user and perform verbing operation on it.
#String should be greater than or equal to 3, else leave unedited
#if string ends with 'ing', replace 'ing' with 'ly'
#add 'ing' if not present

inputStr = input('Enter a string : ')
result = ''
if len(inputStr) >= 3:
	if inputStr.endswith('ing') :
		result = inputStr.replace('ing', 'ly')
	else:
		result = inputStr+'ing'
else :
	result = inputStr
print (result)