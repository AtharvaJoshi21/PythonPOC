#WAP to accept a number from user and check if it's prime

def CheckPrime(inputNum):
	maxRange = int(inputNum / 2)
	for denominator in range(3, maxRange, 2):
		result = int(inputNum % denominator)
		print (result)
		if result == 0:
			return False
	else:
		return True

def main():
	inputNum = eval(input('Please enter a number: '))
	
	if CheckPrime(inputNum):
		print ('Number is prime')
	else:
		print ('Number is not prime')

if __name__ == '__main__':
	main()