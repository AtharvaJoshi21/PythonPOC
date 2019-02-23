# WAP to accept list of intergers and check list is palindrome of not.

def IfPalindrome(inputList):
    i = 0
    j = -1
    k = 0
    
    #Find mid index of list by dividing it by 2 (Floor division)
    listLenMid = len(inputList)//2
    
    while k <= listLenMid:
        #Compare elements a i and j respectively and 
        #check if they're equal.
        if inputList[i] == inputList[j]:
            i += 1
            j -= 1
            k += 1
        #If not equal return False as the list is not palindrome
        else:
            return False
    return True
    
def main():
    inputList = eval(input('Please enter a list : '))
    if IfPalindrome(inputList):
        print('List is a palindrome!')
    else:
        print('List is NOT palindrome!')

if __name__ == '__main__':
    main()