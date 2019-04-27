# WAP to demo map function in Python

from functools import reduce

def Square(x):
    return x*x

def IsEven(x):
    return (x&1) == 0

def Multiply(x, y):
    return x*y

def main():
    even = filter(IsEven, range(1,30))
    x = map(Square, range(1,30,2))
    y = map(lambda sq: sq*sq, range(1,30,2))
    print(reduce(Multiply, range(1,10)))
    print("Even numbers")
    for data2 in even:
        print(data2)
    print("Map square")
    for data in x:
        print(data)
    print("Map lambda")
    for data1 in y:
        print(data1)

if __name__ == "__main__":
    main()