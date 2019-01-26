#WAP to accept three numbers from user and print maximum of them.

def MaximumNum(num1, num2, num3):
	if (num1 > num2 and num1 > num3) :
		return (num1)
	elif (num2 > num3) :
		return (num2)
	else :
		return (num3)

num1, num2, num3 = eval(input("Please enter three numbers: "))

print ('The greatest number is :')

print (MaximumNum(num1, num2, num3))