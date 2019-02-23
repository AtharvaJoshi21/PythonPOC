# WAP to accept an unsorted list of integers from user and sort it using 
# 	a. Bubble Sort
# 	b. Insertion Sort

def BubbleSort(inputList):
    listCount = len(inputList)
    for x in range(listCount - 1):
        alreadySorted = True
        print('Iteration', x)
        for y in range(x+1, listCount - 1):
            if inputList[x] > inputList[y]:
                temp = inputList[x]
                inputList[x] = inputList[y]
                inputList[y] = temp
                alreadySorted = False
            else:
                alreadySorted = True
        if alreadySorted:
            continue

    return inputList

def main():
    unsortedList = eval(input('Please enter a list to be sorted: '))
    print(BubbleSort(unsortedList))

if __name__ == '__main__':
    main()