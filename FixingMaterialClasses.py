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
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 50
        self.fullness -= 10

    def play_DOTA(self):
        print('{} поиграл'.format(self.name))
        self.fullness -= 10


ivan = Man(name='Иван')
print(ivan)

ivan.eat()
print(ivan)
ivan.work()
print(ivan)
ivan.play_DOTA()
print(ivan)