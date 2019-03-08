# WAP to accept a file from user and print it line by line

def PrintFile(inputFilePath):
    fd = open(inputFilePath)

    if fd != None:
        line = fd.readline()
        while line != '':
            print(line)
            line = fd.readline()
        else:
            print('End of file reached!')
    else:
        print('File does not exist!')

def main():
    inputFilePath = input('Please enter name of file: ')
    PrintFile(inputFilePath)

if __name__ == "__main__":
    main()