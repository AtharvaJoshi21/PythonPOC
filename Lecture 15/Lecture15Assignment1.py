# WAP to accept a sentence from user and return a dictionary containing count of each characters occurring in it
#    e.g. India is my country => {a:1, I: 3...}

def CharacterCount(inputStr):
    resultDict = dict()
    for char in inputStr:
        # Check whether key is present in dictionary
        # If not then add else increment count
        if resultDict.get(char) == None:
            resultDict[char] = 1
        else:
            resultDict[char] += 1
    
    return resultDict

def main():
    inputStr = input('Please enter sentence: ')
    print(CharacterCount(inputStr))

if __name__ == "__main__":
    main()