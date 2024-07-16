# This code is going to depict the use of inheritance in classes
class Member():
    def __init__(self,name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
    
class Student(Member):
    def __init__(self, name, level):
        super().__init__(name)
        self.level=level
    def __str__(self) -> str:
       return(f"{self.name} {self.level}")

class Lecturer(Member):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level
    def __str__(self) -> str:
        return(f"{self.name} {self.level}")

member = Member("James")
student = Student("Daniel", "400")
lect = Lecturer("Oko", "300") 

print(student)