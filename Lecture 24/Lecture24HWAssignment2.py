# WAP to implement menu driven Employee management system.
#   - Implement onboard, kick, appraise
#   - Awards - maintain list of awards

class Employee:
    employeeId = 1 #Class attribute for global employee id which will be auto incremented
    def __init__(self, firstName, lastName, gender, marritalStatus, contactNum, emailId, address, annualSalary, department):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__gender = gender
        self.__marritalStatus = marritalStatus
        self.__contactNum = contactNum
        self.__address = address
        self.__annualSalary = annualSalary
        self.__emailId = emailId
        self.__department = department
        self.__employeeId = Employee.employeeId
        self.__isActive = False
        self.__awardsReceived = dict()
        Employee.employeeId += 1
    
    def __repr__(self):
        return "********Employee Info********\nEmployeeId: {0}\nName: {1}\nAddress: {2}\nContact: {3}\nEmailId: {4}\nDepartment: {5}\nAnnual Salary: {6}\nIs Onboarded: {7}\n******** End ********".format(str(self.__employeeId), str(self.__firstName + " " + self.__lastName), str(self.__address), str(self.__contactNum), str(self.__emailId), str(self.__department), str(self.__annualSalary), str(self.__isActive))

    def getEmployeeId(self):
        return self.__employeeId

    def updateMarritalStatus(self, updatedStatus):
        self.__marritalStatus = updatedStatus
        return True

    def updateName(self, updatedfirstName, updatedlastName):
        if self.__gender == "F" and self.__marritalStatus == "UM":
            self.__firstName = updatedfirstName
            self.__lastName = updatedlastName
        else:
            return False
        return True

    def updateContactNum(self, updatedContactNum):
        self.__contactNum = updatedContactNum
        return True

    def updateAddress(self, updatedAddr):
        self.__address = updatedAddr
        return True
    
    def updateEmailId(self, updatedEmail):
        self.__emailId = updatedEmail
        return True
    
    def updateDepartment(self, updatedDept):
        self.__department = updatedDept
        return True
    
    def updateAwardsReceived(self, awardCategory):
        if self.__awardsReceived[awardCategory] == None:
            self.__awardsReceived[awardCategory] = 1
        else:
            self.__awardsReceived[awardCategory] += 1
        return True

    def getMonthlySalary(self):
        return self.__annualSalary // 12

    def OnBoard(self):
        self.__isActive = True
    
    def KickEmployee(self):
        self.__isActive = False
    
    def AppraiseEmployee(self, appraisalBy):
        self.__annualSalary = int(self.__annualSalary) + appraisalBy
    
class EmployeeManager:
    def __init__(self, noOfEmployees):
        self.__noOfEmployees = noOfEmployees
        self.__totalEmployees = dict()
        self.__activeEmployees = dict()
        self.__inactiveEmployees = dict()

    def getAllEmployees(self):
        return self.__totalEmployees

    def assignNewEmployee(self, firstName, lastName, gender, marritalStatus, contactNo, emailId, address, annualSalary, department):
        empObj = Employee(firstName, lastName, gender, marritalStatus, contactNo, emailId, address, annualSalary, department)
        self.__totalEmployees[empObj.getEmployeeId()] = empObj
    
    def onBoardEmployee(self, employeeId):
        if employeeId in self.__totalEmployees:
            empObj = self.__totalEmployees[employeeId]
            empObj.OnBoard()
            self.__activeEmployees[employeeId] = empObj
        else:
            return False
        return True
    
    def kickEmployee(self, employeeId):
        if employeeId not in self.__totalEmployees:
            return False
        elif employeeId in self.__activeEmployees:
            empObj = self.__activeEmployees.pop(employeeId)
            empObj.KickEmployee()
            self.__inactiveEmployees[employeeId] = empObj
        else:
            return False
        return True

    def appraiseEmployee(self, employeeId, appraisalBy):
        if employeeId not in self.__totalEmployees or employeeId not in self.__activeEmployees:
            return False
        else:
            empObj = self.__activeEmployees[employeeId]
            empObj.AppraiseEmployee(appraisalBy)
            self.__activeEmployees[employeeId] = empObj
            self.__totalEmployees[employeeId] = empObj
        return True

    def updatedAwards(self, employeeId, awardCategory):
        if employeeId not in self.__totalEmployees or employeeId not in self.__activeEmployees:
            return False
        else:
            empObj = self.__activeEmployees[employeeId]
            empObj.updateAwardsReceived(awardCategory)
            self.__activeEmployees[employeeId] = empObj
            self.__totalEmployees[employeeId] = empObj
        return True

def UnitTestEmployee():
    empObj = Employee("Atharva", "Joshi", "M", "UM", "9158424824", "someone@example.com", "Pune", "680000", "Development")
    print(empObj)
    empObj.AppraiseEmployee(20000)
    print(empObj)

def UnitTestEmployeeMgr():
    empMgr = EmployeeManager(3)
    empMgr.assignNewEmployee("Atharva", "Joshi", "M", "UM", "9158424824", "someone@example.com", "Pune", "680000", "Development")
    empMgr.assignNewEmployee("Benjamin", "Franklin", "M", "UM", "8888899999", "someone2@example.com", "New York", "680000", "Development")
    empMgr.assignNewEmployee("Jessica", "Doe", "F", "UM", "9999988888", "someone3@example.com", "California", "680000", "Development")
    print(empMgr.getAllEmployees())
    empMgr.onBoardEmployee(1)
    empMgr.onBoardEmployee(2)
    empMgr.onBoardEmployee(3)
    print(empMgr.getAllEmployees())
    empMgr.kickEmployee(2)
    print(empMgr.getAllEmployees())

def main():
    UnitTestEmployeeMgr()

if __name__ == "__main__":
    main()
