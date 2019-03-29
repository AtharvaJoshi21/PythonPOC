# WAP to accept a filename from user and no of lines to be copied to another file. Accept inputs as cmd line params.
#   - Hint use "argparse" module
import shutil
import optparse

def CopyLines(srcFilePath, destFilePath, countOfLines=0):
    srcFile = open(srcFilePath)
    destFile = open(destFilePath, "w")
    line = srcFile.readline()
    count = 0
    
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
    parser = optparse.OptionParser()

    # Setup arguments list
    # parser.add_option("")
    parser.add_option("-i", type = str, help = "Input / Source File Name", dest = "input")
    parser.add_option("-d", type = str, help = "Output / Destination File Name", dest = "output")
    parser.add_option("-n", type = int, help = "Number of lines to be copied, default 0", dest = "numArgs", default = 0)

    # Parse the arguments into list
    (options, args) = parser.parse_args()
    # Invoke copy function
    CopyLines(options.input, options.output, options.numArgs)
    # print(options['i'])
    # print(args)
    print("File copy successful!")

if __name__ == "__main__":
    main()