# WAP to accept a file from user and print those lines who have <= 80 characters. Also print line numbers which have more than 80 characters stating that lines are having more than standard count of characters

def PrintValidLines(inputFile):
    line = inputFile.readline()
    i = 1
    while line != '':
        if len(line) <= 80:
            # print("**** Valid lines ****")
            print(line)
        elif len(line) > 80:
            print("Invalid Line number", i)
            #print(line)
        i += 1
        line = inputFile.readline()
    else:
        print("**** End of File Reached ****")

def main():
    inputFilePath = input("Please enter filename to be read: ")
    fd = open(inputFilePath)
    if fd != None:
        PrintValidLines(fd)
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()