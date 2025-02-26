class a:
    def __init__(self, animal, number):
        self.animal = animal
        self.number = number

    def __add__(self, b):
        c = self
        c.animal = f"{self.animal} и {b.animal}"
        c.number = self.number + b.number
        return c


cat_12 = a("Кот", 12)
dog_14 = a("Собака", 14)

cat_and_dog = cat_12 + dog_14

print(f"{cat_and_dog.animal}, {cat_and_dog.number}")
