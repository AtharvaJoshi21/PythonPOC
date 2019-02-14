#WAP to accept a string from user and print count of consonants in it

def CountConsonants(inputStr):
    count = 0
    for x in inputStr:
        if x not in ('aeiouAEIOU'):
            count += 1
    return count

def main():
    inputStr = input('Please enter a string : ')
    print ('Number of consonants: ', CountConsonants(inputStr))

if __name__ == '__main__':
    main()