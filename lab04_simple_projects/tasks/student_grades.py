class Student:
    """Задача: student_grades"""
    def __init__(self, name: str):
        self.grades = []

    def add_grade(self, g: int):
        self.grades.append(g)
        pass

    def average(self) -> float:
        return sum(self.grades) / len(self.grades)
        pass
