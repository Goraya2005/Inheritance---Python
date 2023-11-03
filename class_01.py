
class Teacher():
    def __init__(self, Teacher_id: int, Teacher_Name : str) -> None:
        self.Teacher_Name : str = Teacher_Name
        self.Teacher_id : int = Teacher_id

    def speaking(self, words) -> None:
        print(f"{self.Teacher_Name} is speaking {words}")

    def Teaching(self, words) -> None:
        print(f"{self.Teacher_Name} is Teaching {words}")

Teacher1 = Teacher(1, "Goraya")

print(f" The Teacher ID of first Teacher is {Teacher1.Teacher_id} and The Name of first Teacher is Mr. {Teacher1.Teacher_Name}")




class Mother():
    def __init__(self, name : str) -> None:
        self.name : str = name
        self.eye_color : str = "Blue"

class Father():
    def __init__(self, name : str) -> None:
        self.name : str = name
        self.hair : str = "Brown"

class Child(Mother, Father):
    def __init__(self, mother_name, father_name, child_name) -> None:
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.name = child_name

Cla : Child = Child("A", "B", "Cla")
print(f"Mother Name of Cla is {Cla.eye_color}")

