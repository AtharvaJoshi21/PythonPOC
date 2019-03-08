# WAP to accept a filename from user and print it in reverse order. Lines should be read only once and not using "readlines()" [Hint: Recursion]

def RevPrintFileContent(inputFile, nextLine):
    if nextLine == '':
        return "End of file"
    else:
        RevPrintFileContent(inputFile, inputFile.readline())
        print(nextLine)

def main():
    inputFilePath = input("Please enter a filename : ")
    fd = open(inputFilePath)
    RevPrintFileContent(fd, fd.readline())

if __name__ == "__main__":
    main()