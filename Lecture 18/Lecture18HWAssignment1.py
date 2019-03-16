# WAP to accept a filename from user and print its statistical information, like type of file, size of file, permissions.
#    - Hint - Use "stat" and "fsts" system calls

import os

def main():
    inputFilePath = input("Please enter a file name: ")
    print("Details are as follows: ")
    print(os.stat(inputFilePath))

if __name__ == "__main__":
    main()