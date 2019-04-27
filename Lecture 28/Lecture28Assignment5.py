# WAP to demo iterator generator in Python

def YieldDemo():
    i = 0
    for i in range(4):
        yield i

def main():
    x = YieldDemo()
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))

if __name__ == "__main__":
    main()