# We are going to use __str__ function in this class program to improve the previous code
class Student:
    def __init__(self, name, stud_form):
        if not name:
            raise ValueError("Invalid Name!")
        if stud_form not in ["Form 1", "Form 2", "Form 3"]:
            raise ValueError("Invalid Form")
        self.name = name
        self.stud_form = stud_form

    def __str__(self):
        return (f"{self.name} is in {self.stud_form}")

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ").capitalize()
    stud_form = input("Form: ").capitalize()

    return Student(name, stud_form)

if __name__ == "__main__":
    main()