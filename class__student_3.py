class Student:
    def __init__(self, name, student_form):

        # Check if user enters no value
        if not name:
            raise ValueError("You need to input a valid name")
        if student_form not in ["Form 1", "Form 2", "Form 3"]:
            raise ValueError("You need to choose either 'Form 1', 'Form 2' or 'Form 3'")
        self.name = name
        self.student_form = student_form

# Main Function
def main():
    student = student_form()
    print(f"{student.name} is in {student.student_form}")

def student_form():
    name = input("Your Name: ")
    student_form = input("Your Form: ")
    return Student(name, student_form)

if __name__ == "__main__":
    main()