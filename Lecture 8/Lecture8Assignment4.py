#WAP to print Fibonacci series starting from 1 to n

def Fibonacci(endIndex):
	a = 1
	b = 1
	print (a,b, end = ' ')
	endIndex = endIndex - 2
	while endIndex > 0:
		c = a + b
		print (c, end = ' ')
		endIndex = endIndex - 1
		a = b
		b = c
	
def main():
	endIndex = eval(input('Please enter number: '))
	Fibonacci(endIndex)

if __name__ == '__main__':
	main()