# WAP to accept a list of integers from user and check if it's sorted or not

def CheckSort(list):
	for x in range(len(list)-1):
		if list[x] < list[x+1]:
			continue
		else:
			return False
	else:
		return True
	
def main():
	listInt = eval(input('Please enter a list to check: '))
	if CheckSort(listInt):
		print ('Sorted')
	else:
		print ('Not Sorted')

if __name__ == '__main__':
	main()