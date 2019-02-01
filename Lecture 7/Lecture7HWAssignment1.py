#WAP to accept a number from user and check if it's a palindrome or not

def CheckPalindrome(inputNo):
	try:
		val = int(inputNo)
		if inputNo == str(val)[::-1]:
			print ('Number is PALINDROME')
		else:
			print ('Number is NOT PALINDROME')
	except ValueError:
		print("That's not an int!")

def main():
	inputNo = input('Please enter a number: ')
	CheckPalindrome(inputNo)

if __name__ == '__main__':
	main()