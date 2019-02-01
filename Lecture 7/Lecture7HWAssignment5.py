#WAP to print star (*) pattern using number of rows taken as user input.

def printStars(rowNo):
	
	for rowCounter in range(1 , rowNo + 1):
		print(' ')
		for rowNum in range(1, rowCounter + 1):
			print('*', end = ' ')

def main():
	inputRowNo = eval(input('Please enter number of rows: '))
	printStars(inputRowNo)

if __name__ == '__main__':
	main()