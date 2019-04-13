# WAP to demonstrate static and class methods in Python

class Demo:
    @staticmethod
    def Invoke():
        print("Static method invoke")

    @classmethod
    def InvokeClassMethod(cls):
        print("Inside class method: ", type(cls), id(cls))
    
    def InvokeObjectMethod(self):
        print("Inside object method")

def main():
    # Demo.Invoke()
    d = Demo()
    print("Printing class method by class")
    Demo.InvokeClassMethod()
    print("Printing class method by object")
    d.InvokeClassMethod()

if __name__ == "__main__":
    main()