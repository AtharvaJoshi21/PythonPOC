#WAP to accept a number from user and check if it's a palindrome or not

def ReverseNumber(inputNo):												#inputno - 543
	remainder = 0
	reversedNo = 0
	while inputNo != 0:														#iteration 1	
		remainder = inputNo % 10											#remainder = 543%10 = 3
		reversedNo = reversedNo * 10 + remainder					#reversedNo = 0*10+3 = 3
		inputNo = int(inputNo // 10)											#inputNo = 543//10 = 54
		
	return reversedNo

def CheckPalindrome(inputNo):
	reversedNo = ReverseNumber(inputNo)
	if inputNo == reversedNo:
		print ('PALINDROME')
	else:
		print ('NOT PALINDROME')

def main():
	inputNo = eval(input('Please enter a number: '))
	CheckPalindrome(inputNo)

if __name__ == '__main__':
	main()