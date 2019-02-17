# WAP to accept a list from user and print it element by element in reverse order using recursion.

def RecursiveReverse(list):
	if len(list) == 0:
		return 'List is empty'
	else:
		RecursiveReverse(list[1::])
		print (list[0])

def main():
	inputList = eval(input('Please enter a list : '))
	RecursiveReverse(inputList)

if __name__ == '__main__':
	main()