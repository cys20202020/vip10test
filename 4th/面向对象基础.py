class Washer():
    # def __init__(self):
    #     self.height = 800
    #     self.width = 500
    # 魔法方法- 初始化方法
    def __init__(self, width, height, brand):
        self.width = width
        self.height = height
        self.brand = brand

    def wash(self):
        # 类里面添加对象属性
        # self.width = 500
        # self.height = 800
        print(f'{self.brand}的长{self.height},高{self.width}')

    # 如果类定义了 __str__ ⽅法，那么就会打印从在这个⽅法中 return 的数据。
    def __str__(self):
        return f'这是{self.brand}的说明书'
    # 当删除对象时，python解释器也会默认调⽤ __del__() ⽅法。
    def __del__(self):
        print(f'我被删除了')

# 实例化
haier1 = Washer(500, 800, '海尔洗衣机')
# haier1 = Washer()
haier1.wash()
print(haier1)

# del haier1
# 实例化调用类方法
# 类外面添加对象属性
# haier1.height = 800
# haier1.width = 500
# print(f'haier1的洗衣机宽度是{haier1.width}')
# print(f'haier1的高度是{haier1.height}')
# print(f'洗衣机的长{haier1.height},高{haier1.width}')
# haier1.wash()
# # 查看实例的物理内存地址
# print(haier1)
#
# haier2 = Washer()
# print(haier2)

# haier2 = Washer(300, 400)
# haier2.wash()
