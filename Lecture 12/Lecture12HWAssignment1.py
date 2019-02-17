# 1. WAP to demonstrate queue DS using list with following menu driven interfaces
# 	a. Enqueue 
# 	b. Dequeue 
# 	c. IsQueueEmpty 
# 	d. IsQueueFull

def IsQueueEmpty(queue):
    if len(queue) == 0:
        return True
    return False

def IsQueueFull(queue):
    if len(queue) == 10:
        return True
    return False

def Enqueue(queue, data):
    queue.append(data)

def Dequeue(queue):
    queue.pop(0)

def QueueOperations():
    ch = 0
    inputQueue = eval(input('Please initialize queue : '))
    
    while ch != 3:
        print('1. Enqueue')
        print('2. Dequeue')
        print('3. Exit')
        ch = eval(input('Please select an operation: '))
        if ch == 1:
            if IsQueueFull(inputQueue):
                print('Queue is full')
            else:
                inputData = eval(input('Please enter data to be entered: '))
                Enqueue(inputQueue, inputData)
                print(inputQueue)
        elif ch == 2:
            if IsQueueEmpty(inputQueue):
                print('Queue is empty')
            else:
                Dequeue(inputQueue)
                print(inputQueue)
        elif ch == 3:
            print('Goodbye!')
            break
        else:
            print('Invalid Choice!')

def main():
    print('Main started!')
    QueueOperations()

if __name__ == '__main__':
    main()