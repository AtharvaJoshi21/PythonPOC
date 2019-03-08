# WAP to accept a filename from user and print those lines which have "the" more than once.

def IsFilterConditionReached(inputStr, filterCriteriaKeyword):
    wordsInLine = inputStr.split(' ')
    count = 0
    # print("filter criteria is ", filterCriteriaKeyword)
    # print("words are ", wordsInLine)
    for word in wordsInLine:
        # print("word is ", word)
        if word == filterCriteriaKeyword:
            count += 1
        if count > 1:
            return True
        else:
            continue
    else:
        return False


def PrintFilteredSentences(inputFile, filterCriteriaKeyword):
    nextLine = inputFile.readline()
    lineNo = 1
    while nextLine != '':
        if IsFilterConditionReached(str(nextLine), filterCriteriaKeyword):
            print(nextLine)
        
        nextLine = inputFile.readline()
        lineNo += 1


def main():
    inputFilePath = input("Please enter a filename : ")
    inputFilterCriteria = input("Please enter keyword : ")
    fd = open(inputFilePath)
    PrintFilteredSentences(fd, inputFilterCriteria)

if __name__ == "__main__":
    main()