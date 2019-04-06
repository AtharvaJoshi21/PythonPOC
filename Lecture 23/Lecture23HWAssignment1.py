# WAP to demo implementation of Queue using classes in Python. [Menu driven]

class Queue:
    def __init__(self, size):
        print("Queue is constructed with size {}".format(str(size)))
        self.__queue = []
        self.__size = size
    
    def __del__(self):
        del self.__queue

    def DisplayQueue(self):
        return self.__queue
    
    def IsEmpty(self):
        return self.__queue == []
    
    def IsFull(self):
        return len(self.__queue) == self.__size
    
    def EnQueue(self, inputData):
        if self.IsFull():
            return False
        else:
            self.__queue.append(inputData)
            return True
    
    def DeQueue(self):
        if self.IsEmpty():
            return -1
        else:
            return self.__queue.pop(0)

def DisplayMenu(q):
    ch = 1
    while ch > 0:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Exit")
        ch = eval(input("Please select your choice: "))
        if ch == 1:
            inputData = eval(input("Please enter the data to be queued: "))
            result = q.EnQueue(inputData)
            if result == True:
                print("Data input successful!")
                print(q.DisplayQueue())
            else:
                print("Queue is full!")
        elif ch == 2:
            result = q.DeQueue()
            if result == -1:
                print("Queue is empty!")
            else:
                print("{} is removed!".format(str(result)))
        elif ch == 3:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
            continue

def main():
    queueSize = eval(input("Please enter size of queue: "))
    queue = Queue(queueSize)
    DisplayMenu(queue)

if __name__ == "__main__":
    main()    
