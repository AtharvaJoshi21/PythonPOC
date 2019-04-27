# WAP to accept a list of nos from user and write a generator to return prime numbers in it.

def CheckPrime(inputNum):
	maxRange = int(inputNum / 2)
	for denominator in range(3, maxRange, 2):
		result = int(inputNum % denominator)
		# print (result)
		if result == 0:
			return False
	else:
		return True

def GetPrimes(inputNosList):
    for number in inputNosList:
        if CheckPrime(number):
            yield number

def main():
    inputNosList = eval(input("Please enter list of numbers: "))
    primeIter = GetPrimes(inputNosList)
    for prime in primeIter:
        print(prime)

if __name__ == "__main__":
    main()