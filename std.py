class Student:
    student_dictionary = {}
    school_name = "XYZ"

    def __init__(self):
        self.roll_no = input("\n\tEnter The Student Roll Number: ")
        self.name = input("\n\tEnter The Student Name: ")
        self.phone_number = input("\n\tEnter The Student Phone Number: ")
        self.address = input("\n\tEnter The Student Address: ")
        student_class = input("\n\tEnter The Student Class [1-10]: ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentlist.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentlist.append(self)

        self.student_class = StudentClass.classes[student_class]
        Student.student_dictionary[self.roll_no] = self

        print("\n\tStudent Added Successfully")
        self.getstudent()

    def getstudent(self):
        print("\n  Student Details  \n")
        print("\tRoll Number:", self.roll_no)
        print("\tName:", self.name)
        print("\tPhone Number:", self.phone_number)
        print("\tAddress:", self.address)
        print("\tClass:", self.student_class.name)
        print("\tSchool Name:", Student.school_name)

    def updatestudent(self):
        print("\n\tSelect option to update student details\n")
        print("\t1. Change Student Name")
        print("\t2. Change Student Phone Number")
        print("\t3. Change Student Address")
        print("\t4. Change Student Class\n")

        option = input("\tEnter option: ")

        if option == "1":
            self.name = input("\tEnter new name: ")
        elif option == "2":
            self.phone_number = input("\tEnter new phone number: ")
        elif option == "3":
            self.address = input("\tEnter new address: ")
        elif option == "4":
            new_class = input("\tEnter new class: ")
            self.student_class.studentlist.remove(self)

            if new_class in StudentClass.classes:
                self.student_class = StudentClass.classes[new_class]
            else:
                self.student_class = StudentClass(new_class)

            self.student_class.studentlist.append(self)
        else:
            print("\tWrong option")
            return

        print("\n\tStudent Updated Successfully")
        self.getstudent()

    @classmethod
    def updateschoolname(cls, new_school_name):
        cls.school_name = new_school_name

    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_dictionary)


class StudentClass:
    classes = {}

    def __init__(self, name):
        self.name = name
        self.studentlist = []
        StudentClass.classes[name] = self


def main():
    print(f"\nWelcome to {Student.school_name} School\n")
    print("1. Get Student Details")
    print("2. Add New Student")
    print("3. Remove Student")
    print("4. Update Student Details")
    print("5. Update School Name")
    print("6. Get Number of Students")
    print("7. Get All Student Details")
    print("8. Get Class Student Details")

    option = input("\nEnter option: ")

    if option == "1":
        roll = input("Enter Roll Number: ")
        if roll in Student.student_dictionary:
            Student.student_dictionary[roll].getstudent()
        else:
            print("Student not found")

    elif option == "2":
        Student()

    elif option == "3":
        roll = input("Enter Roll Number: ")
        if roll in Student.student_dictionary:
            stu = Student.student_dictionary.pop(roll)
            stu.student_class.studentlist.remove(stu)
            print("Student Deleted Successfully")
        else:
            print("Student not found")

    elif option == "4":
        roll = input("Enter Roll Number: ")
        if roll in Student.student_dictionary:
            Student.student_dictionary[roll].updatestudent()
        else:
            print("Student not found")

    elif option == "5":
        name = input("Enter new school name: ")
        Student.updateschoolname(name)
        print("School name updated")

    elif option == "6":
        print("Total Students:", Student.getTotalStudentCount())

    elif option == "7":
        for stu in Student.student_dictionary.values():
            stu.getstudent()

    elif option == "8":
        cname = input("Enter class name: ")
        if cname in StudentClass.classes:
            for stu in StudentClass.classes[cname].studentlist:
                stu.getstudent()
        else:
            print("Class not found")


if __name__ == "__main__":
    choice = "y"
    while choice.lower() == "y":
        main()
        choice = input("\nDo you want to continue (y/n): ")
