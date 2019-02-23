# WAP to use reversal of container, based on it's type, using recursion

def ReverseString(inputStr):
	if len(inputStr) == 0:
		return inputStr
	revStr = ReverseString(inputStr[1:])
	return revStr + inputStr[0]
	
def ReverseList(inputList):
	if len(inputList) == 0:
		return inputList
		
	resultContainer = ReverseList(inputList[1:])
	resultContainer.append(inputList[0])
	return resultContainer

def ReverseContainerMenu():
    ch = 0

    #Display menu
    print('1. Reverse String')
    print('2. Reverse List')
    print('3. Exit')

    while ch != 3:
        #Accept choice from user
        ch = eval(input('Please enter your choice : '))
        if ch == 1:
            inputString = input('Please enter a string to be reversed : ')
            print(ReverseString(inputString))
        elif ch == 2:
            inputList = eval(input('Please enter a list to be reversed : '))
            print(ReverseList(inputList))
        elif ch == 3:
            print('Goodbye!')
            break
        else:
            print('Invalid Choice')
	
def main():
	ReverseContainerMenu()

if __name__ == '__main__':
	main()