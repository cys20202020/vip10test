'''
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤

分析  ：   人 是一个  类
          属性：姓名、运动、食物、体重
'''


class Test_likes():
    def __init__(self, name):
        self.name = name

    def likes(self, sport, food):
        self.sport = sport
        self.food = food
        print(f'{self.name}爱{self.sport},爱吃{self.food}')

    def pweight(self, weight):
        self.weight = weight
        print(f'{self.name}体重是{self.weight}公斤')

    def add(self, food, eat_add):
        self.eat_add = eat_add
        self.food = food
        print(f'每次吃{self.food}会增加{self.eat_add}公斤')

    def reduce(self, sport, sport_reduce):
        self.sport_reduce = sport_reduce
        self.sport = sport
        print(f'每次{self.sport}会减{self.sport_reduce}公斤')


one = Test_likes('小明')
one.likes('跑步', '汉堡包')
one.pweight(75.0)
one.reduce('跑步', 0.5)
one.add('东西', 1)
one.add('汉堡包', 1)
xiaomei = Test_likes('小美')
xiaomei.pweight(45.0)
