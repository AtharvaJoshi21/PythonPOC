# WAP to remove all occurrances of given data from list

def RemoveValue(list, value):
	while value in list:
		list.remove(value)

def main():
	list = eval(input('Please enter list : '))
	inputValue = eval(input('Please enter a value to be removed: '))
	RemoveValue(list, inputValue)
	print (list)
	
if __name__ == '__main__':
	main()