# WAP to accept a number n from user and return a dictionary of squares from 1 to n.

def PrintSquares(inputNumber):
    resultDict = dict()
    for num in range(1, inputNumber + 1):
        resultDict[num] = num * num
    return resultDict

def main():
    inputNumber = eval(input('Please enter a number : '))
    print(PrintSquares(inputNumber))

if __name__ == "__main__":
    main()