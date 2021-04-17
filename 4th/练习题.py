'''
定义一个老师类

'''


class Teacher():
    def __init__(self, xb, name, kecheng):
        self.xb = xb
        self.name = name
        self.kecheng = kecheng

    def teachercan(self):
        print(f'{self.name}老师,性别{self.xb},教{self.kecheng}课')


one = Teacher("男", "张三", "体育")
one.teachercan()
