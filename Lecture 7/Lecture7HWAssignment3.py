#WAP to perform menu driven arithmetic operations.

def Add(int1, int2):
	return int1 + int2

def Subtract(int1, int2):
	return int1 - int2
	
def Divide(int1, int2):
	return int1 / int2

def Multiply(int1, int2):
	return int1 * int2
	
def main():

	ch = 0
	
	while ch != 5:
		print('1. Addition')
		print('2. Subtraction')
		print('3. Multiplication')
		print('4. Division')
		print('5. Exit')
		ch = eval(input('Please select the operation to perform: '))
		
		if ch > 0 and ch < 5:
			int1, int2 = eval(input('Enter two numbers: '))
		
		if	ch == 1:
			print('Addition is: ', Add(int1,int2))
		elif ch == 2:
			print('Subtraction is: ', Subtract(int1,int2))
		elif ch == 3:
			print('Multiplication is: ', Multiply(int1,int2))
		elif ch == 4:
			print('Division is: ', Divide(int1,int2))	
		elif ch == 5:
			print('Good bye!')
		else:
			print ('Invalid Choice!')

if __name__ == '__main__':
	main()