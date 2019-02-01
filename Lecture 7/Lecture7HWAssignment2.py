#WAP to accept a string from user and check if it's a palindrome or not

def CheckPalindromeString(inputStr):
	if inputStr == inputStr[::-1]:
		print ('Number is PALINDROME')
	else:
		print ('Number is NOT PALINDROME')

def main():
	inputStr	= input('Please enter a string: ')
	CheckPalindromeString(inputStr)

if __name__ == '__main__':
	main()