import random


class Voin:
    HP = 100

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def atack(self, unit):
        unit.HP -= 20
        print(
            f"Атаковал юнит {self.name}.\
                  У юнита {unit.name} осталось {unit.HP} здоровья"
        )


voin_1 = Voin()
voin_1.setName("Max")

voin_2 = Voin()
voin_2.setName("Den")

while (voin_1.HP != 0 and voin_2.HP != 0):
    num = random.choice([0, 1])

    if (num):
        voin_1.atack(voin_2)
    else:
        voin_2.atack(voin_1)

if voin_1.HP == 0:
    print(f'Победил юнит {voin_2.name}')
elif voin_2.HP == 0:
    print(f'Победил юнит {voin_1.name}')
