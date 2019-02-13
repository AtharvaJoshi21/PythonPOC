#WAP to print number pyramid

def NumberPyramid(rowNum):
	for i in range(1, rowNum+1):
		for _ in range (1, rowNum - i + 1):
			print (' ', end = '')
		x = i
		for j in range (1, i * 2):
			print (x, end = '')
			if j < i:
				x = x - 1
			else:
				x = x + 1
		print ()
	
def main():
	inputRows = eval(input('Please enter number of rows: '))
	NumberPyramid(inputRows)

if __name__ == '__main__':
	main()