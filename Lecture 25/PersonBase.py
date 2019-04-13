# Base class for Person Entity

class Person:
    def __init__(self, name, address, dob):
        self.__name = name
        self.__address = address
        self.__dob = dob

    def getName(self):
        return self.__name
    
    def getDob(self):
        return self.__dob
    
    def getAddress(self):
        return self.__address
    
    def updateAddress(self, updatedAddr):
        self.__address = updatedAddr
        return True