class Student:
    ...

def main():
    student = get__full_name()
    print(f"Your full name is {student.name} {student.name}")

def get__full_name():
    studentName = Student()
    studentName.first_name = input("First Name: ")
    studentName.last_name = input("Last Name: ")
    return studentName

if __name__ == "__main__":
    main()