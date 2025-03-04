class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification

    def get_info(self):
        return f"{self.name} {self.surname}, {self.qualification}"

    def __del__(self):
        print(f"До свидания мистер {self.name} {self.surname}")


person1 = Person("Максим", "Торубаров", 3)
person2 = Person("Данил", "Цапаев", 2)
person3 = Person("Иван", "Иванов")

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())

del person3

input()
