# WAP to read input file and read words starting with T/t and ending with E/e from it.
import re

def readRegEx(inputFile):
    data = inputFile.read()
    regExObj = re.compile(r"\bT\w+e\b", re.IGNORECASE)
    for match in regExObj.finditer(data):
        print(match)

def main():
    inputFilePath = input("Please enter source file path: ")
    fd = open(inputFilePath)
    readRegEx(fd)

if __name__ == "__main__":
    main()