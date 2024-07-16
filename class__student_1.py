# Let us replace the  tuple with a dictionary

def main():
    student = get__full_name()

    if student['lName'] != "Kwao":
        student["lName"] = "Tettey"
    print(f"Your name is {student['fName']} {student['lName']}")

def get__full_name():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    return {"fName":first_name, "lName":last_name}

if __name__ == "__main__":
    main()