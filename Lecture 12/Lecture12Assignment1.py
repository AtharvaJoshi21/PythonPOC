#WAP to accept a number from user and find it's length using recursion

def NumLength(inputNo):
	if inputNo == 0:
		return 0
	return 1 + NumLength((inputNo & (inputNo - 1)))
	
def main():
	inputNo = eval(input('Please enter a number : '))
	print (NumLength(inputNo))

if __name__ == '__main__':
	main()