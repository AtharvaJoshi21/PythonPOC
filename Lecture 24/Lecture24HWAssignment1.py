# WAP to implement menu driven Student management system.
#   - Student class should have - Name, Address, DOB, Course, Division, ListOfMarks
#       - Implement Getters and Setters
#       - AddStudent(), SuspendStudent(), UpdateAddress(), UpdateMarks(), PrintAllStudentDetails() and PrintPercentage()

class Student:
    autoRollNo = 1
    def __init__(self, name, address, dob, course, division):
        self.__name = name
        self.__address = address
        self.__dob = dob
        self.__course = course
        self.__division = division
        self.__marks = dict()
        self.__rollNo = Student.autoRollNo
        Student.autoRollNo += 1

    def __repr__(self):
        return "RollNo: {0}\nName: {1}\nAddress:{2}\nDOB: {3}\nCourse: {4}\nDivision: {5}\nMarks: {6}".format(str(self.__rollNo),str(self.__name),str(self.__address),str(self.__dob), str(self.__course), str(self.__division), str(self.__marks))

    def getRollNo(self):
        return self.__rollNo

    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob

    def getAddress(self):
        return self.__address

    def updateAddress(self, address):
        self.__address = address

    def getCourse(self):
        return self.__course

    def updateCourse(self, course):
        self.__course = course
    
    def getDivision(self):
        return self.__division
    
    def updateDivision(self, division):
        self.__division = division
    
    def getListOfMarks(self):
        return self.__marks
    
    def updateMarks(self, subject, marks):
        self.__marks[subject] = marks

class StudentManager():
    def __init__(self, noOfStudents):
        self.__noOfStudents = noOfStudents
        self.__enrolledStudents = dict()
        self.__suspendedStudents = dict()
    
    def getAllStudents(self):
        allStudentsDict = self.__enrolledStudents
        allStudentsDict.update(self.__suspendedStudents)
        return allStudentsDict

    def getEnrolledStudents(self):
        return self.__enrolledStudents

    def enrollStudent(self, name, address, dob, course, division):
        if len(self.__enrolledStudents) == self.__noOfStudents:
            return False
        else:
            stud = Student(name, address, dob, course, division)
            self.__enrolledStudents[stud.getRollNo()] = stud
            return True

    def getSuspendedStudents(self):
        return self.__suspendedStudents
    
    def suspendStudent(self, rollNo):
        if rollNo in self.__suspendedStudents:
            pass
        elif rollNo in self.__enrolledStudents:
            self.__suspendedStudents[rollNo] = self.__enrolledStudents.pop(rollNo)
        else:
            return False
        return True

    def updateMarks(self, rollNo, subject, marks):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.updateMarks(subject, marks)
            return True
        else:
            return False
    
    def updateAddress(self, rollNo, address):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.updateAddress(address)
            return True
        else:
            return False

    def updateDivision(self, rollNo, division):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.updateDivision(division)
            return True
        else:
            return False
    
    def updateCourse(self, rollNo, course):
        if rollNo in self.__enrolledStudents:
            stud = self.__enrolledStudents[rollNo]
            stud.updateCourse(course)
            return True
        else:
            return False
        
    def getStudentDetails(self, rollNo):
        if rollNo in self.__enrolledStudents:
            return self.__enrolledStudents[rollNo]
        else:
            return None

def StudentConstructor():
    inputStudName = input("Please enter name: ")
    inputStudAddress = input("Please enter address: ")
    inputStudDob = input("Please enter date of birth: ")
    inputStudCourse = input("Please enter course name: ")
    inputStudDivision = input("Please enter division: ")
    return (inputStudName, inputStudAddress, inputStudDob, inputStudCourse, inputStudDivision)

def DisplayStudentManagementMenu(studMgr):
    ch = 1
    while ch != 0:
        print("1. Get List of All Students")
        print("2. Get List of Enrolled Students List")
        print("3. Get List of Suspended Students List")
        print("4. Get Details of Student")
        print("5. Enroll Student")
        print("6. Suspend Student")
        print("7. Update Address")
        print("8. Update Division")
        print("9. Update Course")
        print("10. Update Marks")
        print("11. Exit")
        ch = eval(input("Please enter your choice: "))
        if ch == 1:
            print(studMgr.getAllStudents())
        elif ch == 2:
            print(studMgr.getEnrolledStudents())
        elif ch == 3:
            print(studMgr.getSuspendedStudents())            
        elif ch == 4:
            inputRollNo = eval(input("Please enter roll number to be searched: "))
            print(studMgr.getStudentDetails(inputRollNo))
        elif ch == 5:
            (inputStudName, inputStudAddress, inputStudDob, inputStudCourse, inputStudDivision) = StudentConstructor()
            studMgr.enrollStudent(inputStudName, inputStudAddress, inputStudDob, inputStudCourse, inputStudDivision)
        elif ch == 6:
            inputRollNo = eval(input("Please enter roll number to be searched: "))
            isSuspended = studMgr.suspendStudent(inputRollNo)
            if isSuspended:
                print("Operation successful!")
            else:
                print("Student already suspended!")
        elif ch == 7:
            inputRollNo = eval(input("Please enter roll number to be searched: "))
            inputUpdatedAddr = input("Please enter address to be updated: ")
            isAddrUpdated = studMgr.updateAddress(inputRollNo, inputUpdatedAddr)
            if isAddrUpdated:
                print("Address updated successfully!")
            else:
                print("Something went wrong!")
        elif ch == 8:
            inputRollNo = eval(input("Please enter roll number to be searched: "))
            inputUpdatedDivision = input("Please enter division to be updated: ")
            isDivisionUpdated = studMgr.updateDivision(inputRollNo, inputUpdatedDivision)
            if isDivisionUpdated:
                print("Division updated successfully!")
            else:
                print("Something went wrong!")
        elif ch == 9:
            inputRollNo = eval(input("Please enter roll number to be searched: "))
            inputUpdatedCourse = input("Please enter course to be updated: ")
            isCourseUpdated = studMgr.updateCourse(inputRollNo, inputUpdatedCourse)
            if isCourseUpdated:
                print("Course updated successfully!")
            else:
                print("Something went wrong!")
        elif ch == 10:
            inputRollNo = eval(input("Please enter roll number to be searched: "))
            inputSubject = input("Please enter subject for which marks are to be updated: ")
            inputUpdatedMarks = input("Please enter marks: ")
            isMarksUpdated = studMgr.updateMarks(inputRollNo, inputSubject, inputUpdatedMarks)
            if isMarksUpdated:
                print("Marks updated successfully!")
            else:
                print("Something went wrong!")
        elif ch == 11:
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")
            continue

def main():
    inputNoOfStudents = eval(input("Please enter the number of students: "))
    studMgr = StudentManager(inputNoOfStudents)
    DisplayStudentManagementMenu(studMgr)

if __name__ == "__main__":
    main()