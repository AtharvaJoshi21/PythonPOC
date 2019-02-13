#Star pattern reversed

def PrintStarsRev(inputNo):
	for i in range(1, inputNo + 1):
		for _ in range (1, inputNo - i + 1):
			print (' ', end = ' ')
		for _ in range (1, i + 1):
			print ('*', end = ' ')
		print ()

def main():
	inputRows = eval(input('Please enter number of rows: '))
	PrintStarsRev(inputRows)

if __name__ == '__main__':
	main()