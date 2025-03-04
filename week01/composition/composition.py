from composition_classes import Room


width = int(input("Введите ширину комнаты: "))
length = int(input("Введите дллину комнаты: "))
height = int(input("Введите высоту комнаты: "))

r1 = Room(width, length, height)

while True:
    check = input("Добавить окно или дверь? да/нет: ")
    if check == "да":
        x = int(input("Введите ширину окна или двери: "))
        y = int(input("Введите высоту окна или двери: "))
        r1.addWD(x, y)
    elif check == "нет":
        break
    else:
        print('Введите либо "да" либо "нет!"')

width_of_roll = int(input("Введите ширину рулона: "))
length_of_roll = int(input("Введите длину рулона: "))

print(f"Площадь оклеиваемой поверхности: {r1.workSurface()}")
print(
    f"Необходимое количество рулонов: {r1.number_of_rolls(width_of_roll, 
                                                          length_of_roll)}"
)
