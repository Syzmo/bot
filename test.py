
from homework1 import Hero


class FireHero(Hero):

    f = 'огнеупорность'

    def __init__(self, name, nickname, hp, damage, fly = False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def brand_phrase(self):
        if self.fly == True:
            print('fly in the True_phrase')
    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.hp}, {self.damage}, {self.fly}'


class WaterHero(Hero):

    w = 'дыхание под водой'

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass

    def brand_phrase(self):
        if self.fly == True:
            print('fly in the True_phrase')

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.hp}, {self.damage}, {self.fly}'


class LandHero(Hero):

    l = 'управление землёй'

    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def __Gen_x(self):
        pass
    def brand_phrase(self):
        if self.fly == True:
            print('fly in the True_phrase')

    def __str__(self):
        return f'{self.name}, {self.nickname}, {self.hp}, {self.damage}, {self.fly}'



f = FireHero(name='Matt', nickname='fenix', hp=30, damage=2, fly=True)
w = WaterHero(name='nick', nickname='aquaman', hp=45, damage=7, fly=False)
l = LandHero(name='jack', nickname='rock', hp=75, damage=4, fly=False)
Hero_list = [f, w, l]
print(Hero_list)
