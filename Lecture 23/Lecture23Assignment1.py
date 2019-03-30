# WAP to demo implementation of Stack using classes in Python

class Stack:
    def __init__(self, size):
        print("Stack Constructed with size %d"%size)
        self.__stack = []
        self.__size = size
    
    def getStack(self):
        return self.__stack
    
    def __del__(self):
        print("Stack destoyed!")
        del self.__stack
    
    def isEmpty(self):
        return self.__stack == []
    
    def isFull(self):
        return len(self.__stack) == self.__size
    
    def push(self, data):
        if self.isFull():
            return False
        else:
            self.__stack.append(data)
            return True

    def pop(self):
        if self.isEmpty():
            return -1, False
        else:
            return self.__stack.pop(), True

def DisplayMenu(st):
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    ch = 1
    while ch != 4:
        ch = eval(input("Please enter your choice: "))
        if ch == 1:
            inputData = eval(input("Please enter data to be pushed: "))
            isSuccess = st.push(inputData)
            if isSuccess:
                print("Data pushed successfully!")
                print(st.getStack())
            else:
                print("Stack is full!")
        elif ch == 2:
            returnValue, isSuccess = st.pop()
            if isSuccess:
                print("{} is removed".format(str(returnValue)))
                print(st.getStack())
            else:
                print("Stack is empty!")
        elif ch == 3:
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")
            continue
    
def main():
    stackSize = eval(input("Please enter size of stack: "))
    st = Stack(stackSize)
    DisplayMenu(st)

if __name__ == "__main__":
    main()