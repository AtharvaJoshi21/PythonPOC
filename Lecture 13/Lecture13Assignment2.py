# WAP to reverse any container using recursion

def StringRevRecursion(inputStr):
	if len(inputStr) == 0:
		return inputStr
	revStr = StringRevRecursion(inputStr[1:])
	return revStr + inputStr[0]
	
def ReverseContainer(inputContainer):
	if len(inputContainer) == 0:
		return inputContainer
		
	resultContainer = ReverseContainer(inputContainer[1:])
	#if input is a string
	if type(inputContainer) == str:
		return resultContainer + inputContainer[0]
	# If input is list
	resultContainer.append(inputContainer[0])
	return resultContainer
	
def main():
	# inputStr = input('Please enter a string to reverse: ')
	# print (StringRevRecursion(inputStr))
	
	inputContainer = input('Please enter a list to reverse: ')
	print (ReverseContainer(inputContainer))

if __name__ == '__main__':
	main()