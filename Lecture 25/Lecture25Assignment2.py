# WAP to demo multiple inheritence

import inspect

class A():
    def __init__(self):
        print("A initiated")
    def M(self):
        print("M from A class")
    def K(self):
        print("K from A class")

class B(A):
    def __init__(self):
        A.__init__(self)
        print("B Initiated")

    def L(self):
        print("L from B class")

class C(A):
    def __init__(self):
        A.__init__(self)
        print("C Initiated")
    
    def M(self):
        print("M from C class")

class D(B, C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)

def main():
    dObj = D()
    dObj.L()
    dObj.M()
    print(inspect.getmro(D))
    
if __name__ == "__main__":
    main()