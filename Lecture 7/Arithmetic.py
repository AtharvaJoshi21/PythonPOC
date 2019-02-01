#WAP arithmetic.py which contains add, subtract, divide, multiply methods and all accept two integers and call them individually

def Add(int1, int2):
	return int1 + int2 + 10

def Subtract(int1, int2):
	return int1 - int2
	
def Divide(int1, int2):
	return int1 / int2

def Multiply(int1, int2):
	return int1 * int2
	
def main():
	int1, int2 = eval(input('Enter two numbers: '))
	print('Addition is: ', Add(int1,int2))
	print('Subtraction is: ', Subtract(int1,int2))
	print('Division is: ', Divide(int1,int2))
	print('Multiplication is: ', Multiply(int1,int2))

if __name__ == '__main__':
	main()