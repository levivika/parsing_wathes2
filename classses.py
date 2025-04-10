'''
▎Атрибуты класса Student:
1. name (строка) - имя студента.
2. age (целое число) - возраст студента.
3. student_id (строка) - уникальный идентификатор студента.
4. grades (список) - список оценок студента.
5. major (строка) - специальность студента.
▎Методы класса Student:
1. add_grade(grade) - метод для добавления новой оценки в список.
2. get_average_grade() - метод для вычисления средней оценки студента.
3. description() - метод, который возвращает строку с информацией о студенте
(имя, возраст, специальность, средняя оценка).
4. is_passing() - метод, который возвращает True, если средняя оценка больше или
равна 4.5, и False в противном случае.
'''
from reportlab.rl_settings import autoGenerateMissingTTFName


class Student:
    def __init__(self, name, age, student_id, major):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades =[]
        self.major = major
    def add_grade(self, grade):
        self.grades.append(grade)
    def get_average_grade(self):
        if not self.grades:
            return 0
        else:
            return sum(self.grades) / len(self.grades)
    def description(self):
        average_grade = self.get_average_grade()
        return f'(имя-{self.name}, возраст-{self.age}, специальность-{self.major}, средняя оценка-{average_grade:.2f})'
    def is_passing(self):
        average_grade = self.get_average_grade()
        if average_grade >= 4.5:
            return True
        else:
            return False

student = Student('Vika', '17', '01', 'it')
student.add_grade(4)
student.add_grade(5)
student.add_grade(5)
student.add_grade(5)
print(student.description())
print(student.is_passing())


class Dog:
    def __init__(self, name, age, breed, weight, is_vaccinated):
        self.name = name
        self.age = age
        self.breed = breed
        self.weight = weight
        self.is_vaccinated = is_vaccinated
    def bark(self):
        print('Woof')
    def get_human_age(self):
        print(int(self.age) * 7)
    def vaccinate(self):
        if self.is_vaccinated == 'yes':
            return True
        else:
            return False
    def description(self):
        print(f'Dog {self.name}, {self.age} years, {self.breed}')

dog = Dog('Alice', 11, 'chih', 2, 'yes')
dog.bark()
dog.description()
dog.get_human_age()
print(dog.vaccinate())