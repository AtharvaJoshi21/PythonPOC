# WAP to implement Student management system.
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
        
    def getStudentDetails(self, rollNo):
        if rollNo in self.__enrolledStudents:
            return self.__enrolledStudents[rollNo]
        else:
            return None

def UnitTestStudent():
    st = Student("Atharva", "Pune", "21/11/1992", "B.E.", "I.T.")
    print("Roll No: {}".format(st.getRollNo()))
    print("Name: {}".format(st.getName()))
    print("Address: {}".format(st.getAddress()))
    print("Course: {}".format(st.getCourse()))
    print("Division: {}".format(st.getDivision()))
    print("DOB: {}".format(st.getDob()))
    print("Marks: ", st.getListOfMarks())
    st.updateAddress("Sheffield")
    st.updateMarks("DELD", 55)
    st.updateMarks("OOPS", 60)
    st.updateMarks("DSP", 75)
    print("Updated Address: {}".format(st.getAddress()))
    print("Updated Marks: ", st.getListOfMarks())

def UnitTestStudentManager():
    stM = StudentManager(3)
    stM.enrollStudent("Amar", "Delhi", "01/01/1990", "BE", "A")
    stM.enrollStudent("Akbar", "Delhi", "01/02/1991", "BE", "B")
    stM.enrollStudent("Anthony", "Delhi", "01/03/1992", "BE", "C")
    print("********** Enrolled Students are: **********")
    enStu = stM.getEnrolledStudents()
    for st in enStu:
        print(enStu[st])
    stM.suspendStudent(2)
    print("********** Suspended Students are: **********")
    susStu = stM.getSuspendedStudents()
    for st in susStu:
        print(susStu[st])
    print("********** Enrolled Students are: **********")
    enStu = stM.getEnrolledStudents()
    for st in enStu:
        print(enStu[st])
    print("********** Updating Marks **********")
    stM.updateMarks(1, "Algebra", 73)
    print(stM.getEnrolledStudents()[1])

def DisplayStudentManagementMenu(studMgr):
    ch = 1
    while ch != 0:
        print("1. Get List of All Students")
        print("1. Get List of Enrolled Students List")
        print("2. Get List of Suspended Students List")
        print("3. Get Details of Student")
        print("4. Enroll Student")
        print("5. Suspend Student")
        print("6. Update Address")
        print("7. Update Division")
        print("8. Update Course")
        print("9. Update Marks")
        print("10. Exit")
        ch = eval(input("Please enter your choice: "))
        if ch == 1:
            print(studMgr.getEnrolledStudents())
        elif ch == 2:
            print(studMgr.getSuspendedStudents())
        elif ch == 3:
            inputRollNo = eval(input("Please enter roll number to be searched: "))
            print(studMgr.getStudentDetails(inputRollNo))
        elif ch == 4:
            pass
        elif ch == 5:
            pass
        elif ch == 6:
            pass
        elif ch == 7:
            pass
        elif ch == 8:
            pass
        elif ch == 9:
            pass
        elif ch == 10:
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")
            continue

def main():
    # UnitTestStudent()
    # UnitTestStudentManager()
    inputNoOfStudents = eval(input("Please enter the number of students: "))
    studMgr = StudentManager(inputNoOfStudents)
    DisplayStudentManagementMenu(studMgr)

if __name__ == "__main__":
    main()