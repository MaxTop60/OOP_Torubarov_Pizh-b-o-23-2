class Data:
    def __init__(self, *info):
        self.info = list(info)
    
    def __getitem__(self, i):
        return self.info[i]
    

class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)


class Pupil:
    def __init__(self):
        self.knowledge = []
    
    def take(self, info):
        self.knowledge.append(info)

    def forgot(self):
        self.knowledge.pop(0)


pupil = Pupil()
pupil.take('Полиморфизм')
pupil.take('Наследование')
pupil.take('Инкапсуляция')
print(pupil.knowledge)

pupil.forgot()

print(pupil.knowledge)