# WAP to accept unsorted list of integers from user and sort items

def SelectionSort(list):
	for x in range(len(list)-1):
		for y in range(x+1, len(list)):
			if list[x] > list[y]:
				temp = list[x]
				list[x] = list[y]
				list[y] = temp
	
	return list

def SortList(list):
	i = 0
	while i+1 < len(list):
		if list[i] < list[i+1]:
			temp = list[i]
			list[i] = list[i+1]
			list[i+1] = temp
	return list

def main():
	intList = eval(input('Please enter unsorted list: '))
	print (SelectionSort(intList))

if __name__ == '__main__':
	main()