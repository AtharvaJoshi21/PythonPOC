#WAP to accept integer n from user and print tables from 2 to n

inputInt = eval(input('Enter a number: '))

for counter1 in range(2, inputInt+1):
	print ('Printing table for : ', counter1)
	for multiplier in range(1,11):
		print (counter1 * multiplier)
		
print ('Done!')