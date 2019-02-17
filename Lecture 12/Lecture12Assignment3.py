#WAP to implement stack operations on list

def IsEmpty(list):
	if len(list) == 0:
		return True
	return False

def IsFull(list):
	if len(list) == 10:
		return True
	return False

def StackPush(list, data):
	if IsFull(list):
		return False
	else:
		list.append(data)
		return True

def StackPop(list):
	if IsEmpty(list):
		return False
	else:
		list.pop()
		return True

def StackPeep(list):
	return list[-1]

def StackOperations():
	list = []
	data = 0
	ch = 0
	
	print ('1. Push')
	print ('2. Pop')
	print ('3. Peep')
	print ('4. Exit')
	
	ch = eval(input('Please select the operation'))
	while ch > 0 and ch != 4:
		if ch == 1:
			data = eval(input('Please enter data to be pushed: '))
			StackPush(list, data)
			print (list)
			break
		elif ch == 2:
			StackPop(list)
			print (list)
			break
		elif ch == 3:
			if IsEmpty(list):
				print('List is empty!')
			else:
				print(StackPeep(list))
			break
		elif ch == 4:
			pass
		else:
			print ('invalid choice!')

def main():
	StackOperations()

if __name__ == '__main__':
	main()