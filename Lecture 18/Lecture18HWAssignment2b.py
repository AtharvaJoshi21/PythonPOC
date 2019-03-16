# WAP to accept a filename from user and no of lines to be copied to another file. Accept inputs as cmd line params.
#   - Hint use "argparse" module
import shutil
import argparse

def CopyLines(srcFilePath, destFilePath, countOfLines):
    srcFile = open(srcFilePath)
    destFile = open(destFilePath, "w")
    line = srcFile.readline()
    count = 0

    # Unoptimized logic
    # while line != "":
    #     if count > countOfLines and countOfLines > 0:
    #         break
    #     destFile.write(line)
    #     line = srcFile.readline()
    #     count += 1
    # else:
    #     print("Whole file copied successfully!")


    # Optimized logic - using shutil, instead of copying line by line, copy whole object
    if countOfLines == 0:
        shutil.copyfileobj(srcFile, destFile)
        print("Whole file copied successfully!")
    else:
        while line != "":
            if count > countOfLines:
                break
            destFile.write(line)
            line = srcFile.readline()
            count += 1
        else:
            print("Whole file copied successfully!")

    destFile.close()
    srcFile.close()

def main():
    # Invoke argument parser from argparse module
    parser = argparse.ArgumentParser()

    # Setup arguments list
    parser.add_argument("-i", type = str, help = "Input / Source File Name", required = True)
    parser.add_argument("-d", type = str, help = "Output / Destination File Name", required = True)
    parser.add_argument("-n", type = int, help = "Number of lines to be copied, default 0", default = 0)

    # Parse the arguments into list
    args = parser.parse_args()

    # Invoke copy function
    CopyLines(args.i, args.d, args.n)
    print("File copy successful!")

if __name__ == "__main__":
    main()