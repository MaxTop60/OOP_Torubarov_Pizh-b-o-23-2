import random


class Unit:
    def __init__(self, id, team):
        self.id = id
        self.team = team


class Hero(Unit):
    def level_up(self):
        print(f"Поднят уровень героя {self.id}")


class Soldier(Unit):
    def go_to_hero(self, hero: Hero):
        print(f"Солдат {self.id} проследовал за героем {hero.id}")


hero_1 = Hero(1, 1)
hero_2 = Hero(2, 2)

team_1 = []
team_2 = []

for i in range(3, 13):
    if random.choice([1, 2]) == 1:
        team_1.append(Soldier(i, 1))
    else:
        team_2.append(Soldier(i, 2))

team_1_length = len(team_1)
print(f"Число солдат в 1 команде: {team_1_length}")
team_2_length = len(team_2)
print(f"Число солдат во 2 команде: {team_2_length}")

if team_1_length > team_2_length:
    hero_1.level_up()
else:
    hero_2.level_up()

team_1[0].go_to_hero(hero_1)
