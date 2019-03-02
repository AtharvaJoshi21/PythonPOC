# WAP to accept paragraph from user and return a dictionary of count of words in the given paragraph.

def WordCount(inputStr):
    resultDict = dict()
    wordsList = inputStr.split(' ')
    for word in wordsList:
        if resultDict.get(word) == None:
            resultDict[word] = 1
        else:
            resultDict[word] += 1

    return resultDict

def main():
    inputStr = input('Please enter a string : ')
    print(WordCount(inputStr))

if __name__ == "__main__":
    main()