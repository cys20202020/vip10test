'''
分析:
房子类
    实例属性:地址、面积、剩余面积、家具列表
    实例方法：容纳家具
    显示房屋属性：打印
家具类
    属性：家具名称，占地面积
'''


# 定义房子类
class Home():
    # 实例属性
    def __init__(self, address, area):
        # 房子地址
        self.address = address
        # 房子面积
        self.area = area
        # 剩余面积
        self.area_item = area
        # 家具列表
        self.furniture = []

    # 实例方法
    def add_furniture(self, item):
        if self.area_item >= item.area:
            self.furniture.append(item.name)
            #搬入家具后，房屋的剩余面积 =  之前的面积 - 家具的面积
            self.area_item -= item.area
        else:
            print(f'{item.name}太大了，剩余面积不足，无法容纳')

    # 显示房屋属性
    def __str__(self):
        return f'房子在{self.address},房子面积是{self.area},剩余面积{self.area_item},家具有{self.furniture}'


# 定义家具类
class Furniture():
    # 家具类属性
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具面积
        self.area = area


bed = Furniture('床', 6)
jia = Home('beijing', 100)
jia.add_furniture(bed)
print(jia)

around = Furniture('篮球场', 120)
jia.add_furniture(around)
