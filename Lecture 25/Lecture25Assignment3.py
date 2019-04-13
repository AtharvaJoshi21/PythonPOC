# WAP to demo callable object

class Simple:
    def __call__(self):
        print("Simple invoked")

def main():
    S = Simple()
    S()

if __name__ == "__main__":
    main()