# WAP to accept two lists from user and find union of them

def UnionList(inputList1, inputList2):
    unionList = []
    unionList.extend(inputList1)
    
    for x in range(len(inputList2)):
        if inputList2[x] in unionList:
            continue
        else:
            unionList.append(inputList2[x])

    return unionList

def main():
    list1 = eval(input('Please enter first list : '))
    list2 = eval(input('Please enter second list : '))
    print('Union of two lists is: ')
    print(UnionList(list1, list2))

if __name__ == '__main__':
    main()