import random
import termcolor
class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0
# степень сытости, еда, деньги

    def __str__(self):
        return 'Я - {} сытость - {} еды - {} денег - {}'.format(self.name, self.
                                    fullness, self.food, self.money)

    def eat(self):
        if self.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def shopping_for_food(self):
        if self.money >= 50:
            print('{} сходил в магаз за сосисками'.format(self.name))
            self.food += 50
            self.money -= 50
        else:
            print('У персонажа {} нет денег'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        print('{} поиграл'.format(self.name))
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print ('{} умер'.format(self.name))
            return
        dice = random.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping_for_food()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_DOTA()

ivan = Man(name='Иван')

for day in range(1,21):
    termcolor.cprint('============={}==============='.format(day), color='yellow')
    ivan.act()
    print(ivan)