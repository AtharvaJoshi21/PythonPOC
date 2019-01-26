#WAP to accept two strings from user and swap their first two chars

inputStr1 = input('Enter first string: ')
inputStr2 = input('Enter second string: ')

outputStr1 = inputStr2[:2] + inputStr1[2:]

outputStr2 = inputStr1[:2] + inputStr2[2:]

print ('Output is: ')
print (outputStr1)
print (outputStr2)