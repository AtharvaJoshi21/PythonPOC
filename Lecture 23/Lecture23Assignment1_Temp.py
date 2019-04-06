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

    def PrintInteresting(self):
        try:
            print("Interesting: ", self.interesting)
        except:
            print("Not so interesting")
    
def main():
    st = Stack(10)
    st1 = Stack(20)
    st.interesting = True
    st.PrintInteresting()
    st1.PrintInteresting()

if __name__ == "__main__":
    main()