#WAP to accept two numbers from user and print positive subtraction of two.

def SubtractNums(num1, num2):
	subtraction = 0
	if num1 > num2 :
		subtraction = num1 - num2
	else :
		subtraction = num2 - num1
	return subtraction

num1, num2 = eval(input("Enter two numbers : "))

print (SubtractNums(num1, num2))