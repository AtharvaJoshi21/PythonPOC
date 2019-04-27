# WAP to accept multiple email ids from user and print whether all email ids are valid are not.

import re

def validateEmailIds(emailIdList):
    validIds = []
    invalidIds = []

    for emailid in emailIdList:
        matchObj = re.match(r"(\w+\.\w+)@(\w+)\.(\w+)", emailid)
        if matchObj == None:
            invalidIds.append(emailid)
        else:
            validIds.append(emailid)

    return validIds, invalidIds

def main():
    inputEmailId = input("Please enter an emailId to validate: ")
    emailIdList = []
    emailIdList.append(inputEmailId)
    ch = input("Do you want to continue? [Y/N]: ")
    while True:
        if ch == "Y" or ch == "y":
            inputEmailId = input("Please enter an emailId to validate: ")
            emailIdList.append(inputEmailId)
            ch = input("Do you want to continue? [Y/N]: ")
            continue
        else:
            break
    
    (validIds, InvalidIds) = validateEmailIds(emailIdList)
    print("Valid Emaild Ids: ")
    print(validIds)
    print("Invalid Email Ids: ")
    print(InvalidIds)

if __name__ == "__main__":
    main()