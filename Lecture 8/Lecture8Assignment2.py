# Star pattern 3

def StarPattern3(rowNum):
	for i in range (1, rowNum+1):
		for _ in range (1, rowNum-i+1):
			print (' ', end = '')
		for _ in range (1, i * 2):
			print ('*', end = '')
		print ()
		
def main():
	inputRows = eval(input('Please enter number of rows : '))
	StarPattern3(inputRows)

if __name__ == '__main__':
	main()