# WAP to accept two lists from user, sort them and merge two sorted lists, element by element preserving the sort order

def MergeLists(list1, list2):
	i = 0
	j = 0
	list3 = []
	while i < len(list1) and j < len(list2):
		if list1[i] < list2[j]:
			list3.append(list1[i])
			i += 1
		else:
			list3.append(list2[j])
			j += 1
	
	if i < len(list1):
		list3.extend(list1[i:])
	elif j < len(list2):
		list3.extend(list2[j:])
	
	return list3
	
def SortList(list):
	for x in range(len(list)-1):
		for y in range(x+1, len(list)):
			if list[x] > list[y]:
				temp = list[x]
				list[x] = list[y]
				list[y] = temp	

def main():
	inputList1 = eval(input('Please enter first list : '))
	inputList2 = eval(input('Please enter second list: '))
	SortList(inputList1)
	SortList(inputList2)
	print('Merged list is : ')
	print (MergeLists(inputList1, inputList2))

if __name__ == '__main__':
	main()