import random
import termcolor
class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
# степень сытости, еда, деньги

    def __str__(self):
        return 'Я - {} сытость - {}'.format(self.name, self.
                                    fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def shopping_for_food(self):
        if self.house.money >= 50:
            print('{} сходил в магаз за сосисками'.format(self.name))
            self.house.food += 50
            self.house.money -= 50
        else:
            print('У персонажа {} нет денег'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 50
        self.fullness -= 10

    def watching_tv(self):
        print('{} смотрел телевизор'.format(self.name))
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print ('{} умер'.format(self.name))
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping_for_food()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watching_tv()
    def go_into_house(self, house):
        self.house = house
        self.fullness -= 10
        termcolor.cprint('{} заехал на хату'.format(self.name), color='red')
class House:
    def __init__(self):
        self.money = 0
        self.food = 50
    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}'.format(self.food
                                                                  , self.money)
citizens = [
Man(name='Иван'),
Man(name='Петя'),
Man(name='Кенни')
]

my_sweet_house = House()
for citizen in citizens:
    citizen.go_into_house(house=my_sweet_house)

for day in range(1,366):
    termcolor.cprint('============={}==============='.format(day), color='yellow')
    for citizen in citizens:
        citizen.act()
    print('=========================')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_house)