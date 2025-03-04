class Snow:
    def __init__(self, num_of_snowlakes):
        self.num_of_snowlakes = num_of_snowlakes

    def __add__(self, b):
        c = self
        c.num_of_snowlakes = self.num_of_snowlakes + b.num_of_snowlakes
        return c

    def __sub__(self, b):
        c = self
        c.num_of_snowlakes = self.num_of_snowlakes - b.num_of_snowlakes
        return c

    def __mul__(self, b):
        c = self
        c.num_of_snowlakes = self.num_of_snowlakes * b.num_of_snowlakes
        return c

    def __truediv__(self, b):
        c = self
        c.num_of_snowlakes = self.num_of_snowlakes // b.num_of_snowlakes
        return c

    def makeSnow(self, num_in_row):
        string = ""
        i = 0
        while i < self.num_of_snowlakes:
            for el in range(0, num_in_row):
                if i < self.num_of_snowlakes:
                    string += "*"
                    i += 1
                else:
                    break
            string += "\n"
        return string


snow = Snow(33)
print(snow.makeSnow(5))
