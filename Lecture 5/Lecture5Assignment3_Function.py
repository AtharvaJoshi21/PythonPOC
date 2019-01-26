#WAP to accept three numbers from user and print minimum of them.

def MinimumNum(num1, num2, num3):
	if	num1 < num2 and num1 < num3 :
		return (num1)
	elif (num2 < num3) :
		return (num2)
	else :
		return (num3)

num1, num2, num3 = eval(input('Please enter three numbers: '))
print ('The minimum of the three numbers is : ')

print (MinimumNum(num1, num2, num3))