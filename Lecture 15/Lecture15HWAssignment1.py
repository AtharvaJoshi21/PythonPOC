# WAP to accept a sentence which contains upper case and lower case characters. Return a dictionary containing count of total number of lower case and total number of upper case characters.

def CountChars(inputStr):
    resultDict = dict({
        "lowercase": 0,
        "uppercase": 0
    })

    for ch in inputStr:
        if ch.isupper() == True:
            resultDict["uppercase"] += 1
        else:
            resultDict["lowercase"] += 1

    return resultDict

def main():
    inputStr = input('Please enter a string : ')
    print('Number of upper case and lower case characters is: ')
    print(CountChars(inputStr))

if __name__ == "__main__":
    main()