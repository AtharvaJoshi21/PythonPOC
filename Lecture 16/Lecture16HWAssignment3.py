# WAP to accept a config file from user and create a dictionary of config settings defined in it.

import io

# Improper logic
def ParseConfig(inputConfigFile):
    configDict = dict()
    nextLine = inputConfigFile.readline()
    nextLineStr = str(nextLine)
    print(nextLineStr)
    keyValPair = []
    while nextLine != '':
        if nextLineStr.startswith('#'):
            continue
        elif nextLineStr.count(':') > 0 and nextLineStr.count('=') == 0:
            keyValPair = nextLineStr.split(":")
            if keyValPair[1].count('#') > 0:
                configDict[keyValPair[0]] = (keyValPair[1].split('#')[0])
            else:
                configDict[keyValPair[0]] = keyValPair[1]
        elif nextLineStr.count('=') > 0:
            keyValPair = nextLineStr.split('=')
            if keyValPair[1].count('#') > 0:
                configDict[keyValPair[0]] = (keyValPair[1].split('#')[0])
            else:
                configDict[keyValPair[0]] = keyValPair[1]
    
    return configDict

# Optimized code
def ParseConfigurations(inputFile):
    line = inputFile.readline()
    configDict = dict()
    currentCategory = b""
    keyValuePair = []
    while line != b"":
        line = line[:-1]
        if (not line.startswith(b"#")) and line != b"\n":
            if line.startswith(b"["):
                configDict[line] = dict()
                currentCategory = line
            elif (b"=" in line or b":" in line):
                # print(line[:-1])
                if b"=" in line:
                    keyValuePair = line.split(b"=")
                else:
                    keyValuePair = line.split(b":")

                if b"#" in keyValuePair[1]:
                    configDict[currentCategory][keyValuePair[0]] = (keyValuePair[1].split(b"#")[0])
                else:
                    configDict[currentCategory][keyValuePair[0]] = keyValuePair[1]
            
        line = inputFile.readline()
    return configDict

def main():
    inputFilePath = input("Please enter config file name: ")
    fd = io.FileIO(inputFilePath)
    # fd = open(inputFilePath)
    if fd == None:
        print("File not found!")
    else:
        # print(ParseConfig(fd))
        print(ParseConfigurations(fd))

if __name__ == "__main__":
    main()