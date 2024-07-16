# Working with class and @property to get user input

class Student:
    def __init__(self, name, level, lecturer):
        self.name=name
        self.level=level
        self.lecturer = lecturer

    def __str__(self):
        return (f"{self.name} is in Level {self.level}")
    
    def lect(self):
        match self.lecturer:
            case "kofi":
                return("Cool 😎")
            case "ama":
                return("Cute 🥰")
            case "jojo":
                return("Crazy 🤬")
            case _:
                return("😤")

    # Getter Method
    @property
    def level(self):
        return self._level
    
    # Setter Method
    @level.setter
    def level(self, level):
        if level not in ["100", "200", "300", "400"]:
            raise ValueError("Invalid Level")
        self._level = level

    # Getter Setter Method for name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
def main():
    student = get_student()
    print(student, student.lect(), sep=" => ")

def get_student():
    name = input("Name: ")
    level = input("Level: ")
    lecturer = input("Lecturer Name: ")
    # student = Student()

    return Student(name, level,lecturer)

if __name__ == "__main__":
    main()