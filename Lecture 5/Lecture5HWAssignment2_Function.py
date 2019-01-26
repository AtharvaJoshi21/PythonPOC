#WAP to accept number of donuts from user
#Case 1: If number of donuts is more than 10, print "No of donuts is : many"
#Case 2: If number of donuts is less than 10, print "No of donuts is : <Number of donuts>"

def CalculateDonuts(noOfDonuts):
	result = ''
	if noOfDonuts > 10:
		result = 'No of donuts is : many'
	else :
		result = 'No of donuts is : ' + str(noOfDonuts)
	return result

noOfDonuts = eval(input('Enter number of donuts: '))

print (CalculateDonuts(noOfDonuts))