'''
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

'''


class Shoot():
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def __str__(self):
        return f'士兵{self.name}有一把{self.gun}'

    def firestarter(self, action):
        # self.name = name
        self.action = action
        print(f'士兵可以扣动{self.action}开火')

    def send_bullet(self,bullet):
        self.bullet = bullet
        print(f"{self.gun}可以发射{self.bullet}")

    def add(self,bullet,number):
        self.bullet = bullet
        self.number = number
        print(f'{self.gun}可以添加{self.number}发{self.bullet}')



one = Shoot('瑞恩', 'AK47')
print(one)
one.firestarter('扳机')
one.send_bullet('子弹')
one.add('子弹','50')