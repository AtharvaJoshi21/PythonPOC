# WAP to accept two lists from user and find symmetric difference of them (exclude common elements) [l1 - l2 union l2 - l1]

def SymmetricDiffOptimized(inputList1, inputList2):
    resultList = []
    i=0
    j=0
    while i < len(inputList1) and j < len(inputList2):
        if inputList1[i] not in inputList2:
            resultList.append(inputList1[i])
            i += 1
        elif inputList2[j] not in inputList1:
            resultList.append(inputList2[j])
            j += 1
        else:
            i += 1
            j += 1
    
    if i < len(inputList1):
        resultList.extend(inputList1[i::])
    elif j < len(inputList2):
        resultList.extend(inputList2[j::])
    
    return resultList

def SymmetricDiff(inputList1, inputList2):
    diffList1 = []
    diffList2 = []

    # Check if any element of first list is not present in second list
    # If found, add into first diff list
    for i in range(len(inputList1)):
        if inputList1[i] not in inputList2:
            diffList1.append(inputList1[i])
        else:
            continue
    
    # Check if any element of second list is not present in first list
    # If found, add into second diff list
    for j in range(len(inputList2)):
        if inputList2[j] not in inputList1:
            diffList2.append(inputList2[j])
        else:
            continue

    # Merge two difference lists, thus creating symmetric difference (A-B) union (B-A)
    diffList1.extend(diffList2)
    return diffList1

def main():
    list1 = eval(input('Please enter first list: '))
    list2 = eval(input('Please enter second list: '))
    print('Symmetric difference between two lists is : ')
    print(SymmetricDiff(list1, list2))
    print(SymmetricDiffOptimized(list1, list2))

if __name__ == '__main__':
    main()