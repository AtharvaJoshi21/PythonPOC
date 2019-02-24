# WAP to accept two lists from user and find intersection of them

# Function to iterate on smaller lists for lesser iterations
def IterateLists(maxIterationCount, inputList1, inputList2):
    resultList = []
    for i in range(maxIterationCount):
        if inputList1[i] in inputList2:
            resultList.append(inputList1[i])
    return resultList

def IntersectionList(inputList1, inputList2):
    intersectionList = []
    maxIterationCount = 0

    #Check which list has less elements
    if len(inputList1) <= len(inputList2):
        maxIterationCount = len(inputList1)
        intersectionList = IterateLists(maxIterationCount, inputList1, inputList2)
    else:
        maxIterationCount = len(inputList2)
        intersectionList = IterateLists(maxIterationCount, inputList2, inputList1)
    
    return intersectionList

def main():
    list1 = eval(input('Please enter first list: '))
    list2 = eval(input('Please enter second list: '))
    print('Intersection of two lists is : ')
    print(IntersectionList(list1, list2))

if __name__ == '__main__':
    main()