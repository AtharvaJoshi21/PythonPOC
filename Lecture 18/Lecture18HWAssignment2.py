# WAP to accept a filename from user and no of lines to be copied to another file. Accept inputs as cmd line params.

import sys

def CopyLines(srcFilePath, destFilePath, countOfLines):
    srcFile = open(srcFilePath)
    destFile = open(destFilePath, "w")
    line = srcFile.readline()
    count = 1
    while line != "":
        if count > countOfLines:
            break
        destFile.write(line)
        line = srcFile.readline()
        count += 1
    
    destFile.close()
    srcFile.close()

def main():
    sysArgv = sys.argv
    if len(sysArgv) != 4:
        print("Invalid parameters!")
    else:
        CopyLines(str(sysArgv[1]), str(sysArgv[2]), int(sysArgv[3]))
        print("File copy successful!")

if __name__ == "__main__":
    main()