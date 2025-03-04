class Win_Door:
    """Класс окно/дверь"""
    def __init__(self, x, y):
        """Конструктор принимает ширину и высоту окна или двери"""
        self.square = x * y


class Room:
    """Класс комната"""
    def __init__(self, x, y, z):
        """Конструктор принимает длину, ширину и высоту комнаты
        а также инициализирует список окон и дверей"""
        self.width = x
        self.length = y
        self.height = z
        self.wd = []

    def addWD(self, w, h):
        """Заполнение списка окон и дверей, на вход принимается
        ширина и высота добавляемогое окна/двери"""
        self.wd.append(Win_Door(w, h))

    def workSurface(self):
        """Вычисление оклеиваемой площади с учётом площадей окон и дверей"""
        self.square = 2 * self.height * (self.width + self.length)
        for i in self.wd:
            self.square -= i.square
        return self.square

    def number_of_rolls(self, roll_length, roll_width):
        """Вычисление необходимого количества рулонов для обклеивания"""
        return self.workSurface() // (roll_length * roll_width) + 1
