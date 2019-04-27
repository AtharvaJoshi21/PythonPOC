# WAP to create generators of 5,10 and 15 using lambdas.

def Generator(x):
    return lambda n: n + x

def main():
    generator_of_5 = Generator(5)
    print("Generator of 5 =>", generator_of_5(10))

    generator_of_10 = Generator(10)
    print("Generator of 10 =>", generator_of_10(10))

if __name__ == "__main__":
    main()