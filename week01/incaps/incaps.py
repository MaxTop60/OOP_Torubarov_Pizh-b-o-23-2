class A:
    def __init__(self, num, string):
        self.__num = num
        self.__string = string

    def getField(self, attr):
        if attr == "num":
            return self.__num
        elif attr == "string":
            return self.__string
        else:
            print("Такого атрибута нет в классе")

    def setField(self, attr, value):
        if attr == "num":
            self.__num = value
        elif attr == "string":
            self.__string = value
        else:
            print("Такого атрибута нет в классе")


a = A(15, "Да")
print(a.getField("num"))
print(a.getField("string"))


a.setField("string", "Нет")
print(a.getField("num"))
print(a.getField("string"))
