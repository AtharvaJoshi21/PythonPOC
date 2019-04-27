# WAP to accept a filename from user and print all digits from it.

import re

def main():
    inputFilePath = input("Please enter a file name: ")
    fd = open(inputFilePath)
    data = fd.read()
    digitsRegEx = re.compile(r"\d+")
    for match in digitsRegEx.finditer(data):
        print(match)

if __name__ == "__main__":
    main()