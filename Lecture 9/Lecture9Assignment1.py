#WAP to perform addition and multiplication of given numbers (Input upto 5 numbers)

def Multiply(a, b = 1, c = 1, d = 1, e = 1):
    return a*b*c*d*e

def Addition(a, b = 0, c = 0, d = 0, e = 0):
    return a+b+c+d+e

def main():
    print ('Addition Examples are : ')
    print (Addition(2,4))
    print (Addition(2,4,5))
    print (Addition(2,4,5,6))
    print (Addition(2,4,5,6,7))

    print ('Multiplication Examples are : ')
    print (Multiply(2,4))
    print (Multiply(2,4,5))
    print (Multiply(2,4,5,6))
    print (Multiply(2,4,5,6,7))
            
if __name__ == '__main__':
    main()