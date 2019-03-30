# WAP to implement complex number using Class and perform following operations
#   - Add a complex number
#   - Subtract a complex number
#   - Multiply a complex number by an integer

class ComplexNum:
    # Constructor
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    # Destructor
    def __del__(self):
        del self
    
    # Return string representation of object (Similar to ToString() in C#)
    def __repr__(self):
        return "{0} + {1}i".format(str(self.real), str(self.imaginary))

    # Operator overloaded addition method
    def __add__(self, addParam):
        if isinstance(addParam, int):
            return ComplexNum(self.real + addParam, self.imaginary)
        else:
            return ComplexNum(self.real + addParam.real, self.imaginary + addParam.imaginary)

    def Add(self, complexAdd):
        return ComplexNum(self.real + complexAdd.real, self.imaginary + complexAdd.imaginary)
    
    def Subtract(self, complexSub):
        return ComplexNum(self.real - complexSub.real, self.imaginary - complexSub.imaginary)
    
    def Multiply(self, multiplicationFactor):
        return ComplexNum(self.real * multiplicationFactor, self.imaginary * multiplicationFactor)
    
def DisplayMenu(cpNum):
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")
    ch = 1
    while ch != 5:
        ch = eval(input("Please enter your choice: "))
        if ch == 1:
            addReal, addImag = eval(input("Please enter complex number to be added: "))
            print("Result of addition is : ")
            # print(cpNum.Add(ComplexNum(addReal, addImag)))
            print(cpNum + ComplexNum(addReal, addImag))

        elif ch == 2:
            subReal, subImag = eval(input("Please enter complex number to be subtracted: "))
            print("Result of subtraction is : ")
            print(cpNum.Subtract(ComplexNum(subReal, subImag)))

        elif ch == 3:
            multiParam = eval(input("Please enter number to be multiplied with: "))
            print("Result of multiplication is: ")
            print(cpNum.Multiply(multiParam))

        elif ch == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
            continue

def main():
    real, imag = eval(input("Please enter complex number: "))
    cpNum = ComplexNum(real, imag)
    DisplayMenu(cpNum)

if __name__ == "__main__":
    main()