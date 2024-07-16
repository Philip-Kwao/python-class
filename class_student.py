# This program is going to accept the students first name and last name 
class Student:
    ...

# take user input

def main():
    student = get_fullName()
    print(f"Your full name is: {student[0]} {student[1]}")


def get_fullName():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    return first_name, last_name

if __name__=="__main__":
    main()