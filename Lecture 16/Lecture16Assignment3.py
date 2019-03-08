# WAP to accept a file from user and print shortest and longest line from that file.

def PrintShortestLongestLines(inputFile):
    line = inputFile.readline()
    maxLine = line
    minLine = line

    while line != "":
        line = inputFile.readline()

        if line == "\n" or line == "":
            continue

        if len(line) < len(minLine):
            minLine = line
        elif len(line) > len(maxLine):
            maxLine = line

    return minLine, maxLine

def PrintShortestLongestLinesDict(inputFile):
    line = inputFile.readline()
    maxline = len(line)
    minline = len(line)
    resultDict = dict({
        "MinLen": line,
        "MaxLen": line
    })
    while line != '':
        line = inputFile.readline()
        if line == '\n' or line == '':
            continue
        if len(line) < minline:
            resultDict["MinLen"] = line
        elif len(line) > maxline:
            resultDict["MaxLen"] = line
    
    return resultDict

def main():
    inputFilePath = input("Please enter a filename to be read: ")
    fd = open(inputFilePath)
    if fd != None:
        # print(PrintShortestLongestLines(fd))
        minLenLin, maxLenLine = PrintShortestLongestLines(fd)
        print("Min Length {}\nMax Length {}".format(minLenLin, maxLenLine))
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()