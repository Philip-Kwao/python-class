# This program is going use class methods to accept user input and output them

class Student:
    def __init__(self, name,level ):
        self.name = name
        self.level = level

    def __str__(self):
        return (f"{self.name} is in Level {self.level}")
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        level = input("Level: ")
        return cls(name, level)
def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()