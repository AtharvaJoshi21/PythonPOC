#WAP to accept a number and check if it's even or odd without using arithmetic operators

def IsOdd(num):
    if((num & 1) == 0):
        return False
    else:
        return True

def main():
    inputNum = eval(input('Please enter a number: '))
    print('Number is Odd: ', IsOdd(inputNum))

if __name__ == '__main__':
    main()