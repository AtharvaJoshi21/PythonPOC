#WAP to accept number of donuts from user
#Case 1: If number of donuts is more than 10, print "No of donuts is : many"
#Case 2: If number of donuts is less than 10, print "No of donuts is : <Number of donuts>"

noOfDonuts = eval(input('Enter number of donuts: '))

if noOfDonuts > 10:
	print ('No of donuts is : many')
else :
	print ('No of donuts is : ', noOfDonuts)