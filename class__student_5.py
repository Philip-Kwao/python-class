# Lets add another instance variable to the class
class Student:
    def __init__(self, name, stud_level, patron):
        if not name:
            raise ValueError("Invalid Name")
        if stud_level not in ["100", "200", "300", "400"]:
            raise ValueError("Invalid Student Level choose either 100, 200, 300 or 400")
        self.name = name
        self.stud_level = stud_level
        self.patron = patron
    
    
    def __str__(self):
        return (f"{self.name} is in {self.stud_level}")
    
    def patron_attitude(self):
        match self.patron:
            case "Gavua":
                return("🎠")
            case "Torkudzo":
                return("😜")
            case "Koby":
                return("😎")
            case _:
                return("😤")
        

def main():
    student = get_student()
    print(student.patron_attitude())

def get_student():
    name = input("Name: ").capitalize()
    stud_level = input("Level: ").capitalize()
    patron = input("Patron Name: ").capitalize()
    return (Student(name, stud_level, patron))


if __name__ == "__main__":
    main()