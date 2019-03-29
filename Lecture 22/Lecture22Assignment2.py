# WAP to accept an input file name, output file name and error file name from user using subprocess.Popen. Ensure that word count, char count and line count of input file are returned to output file.

import subprocess

def PrintFileStat(inputFile, outputFile, errFile):
    subprocess.Popen(['wc', '-m', '-l', '-w'], stdin=inputFile, stdout=outputFile, stderr=errFile)
    inputFile.close()
    outputFile.close()
    errFile.close()
    print("Process completed!")

def main():
    inputFilePath = input("Please enter input file path : ")
    outputFilePath = input("Please enter output file path : ")
    errorFilePath = input("Please enter error file path : ")
    inputFile = open(inputFilePath)
    outputFile = open(outputFilePath, "w")
    errorFile = open(errorFilePath, "w")
    PrintFileStat(inputFile, outputFile, errorFile)

if __name__ == "__main__":
    main()