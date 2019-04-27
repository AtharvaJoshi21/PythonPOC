# Class definition for Library Member entity

class Member:
    __MemberId = 1
    def __init__(self, name, address, contactNo):
        self.__MemberId = Member.__MemberId
        Member.__MemberId += 1
        self.__name = name
        self.__address = address
        self.__contactNo = contactNo
        self.__isActive = True
        self.__borrowedBooks = dict()
    
    def __repr__(self):
        return "\nMember Id: {0}\nName: {1}\nAddress: {2}\nContact Number: {3}\nBooks borrowed: {4}".format(str(self.__MemberId), str(self.__name), str(self.__address), str(self.__contactNo), str(self.__borrowedBooks))
    
    def get