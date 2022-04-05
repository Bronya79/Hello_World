class Car():
    price = 30000

    def __init__(self, name):
        self.name = name
        self.color = ""

    def setColor(self, color):
        self.color = color


class Ecar(Car):
    def __init__(self, name):
        super().__init__(name)  # 初始化父类的属性
        self.battery_size = 300

    def getEcar(self):
        print('我是电动汽车' + self.name + '电瓶车容量为' + str(self.battery_size) + '公里')


my_tesla = Ecar('特斯拉')
my_tesla.getEcar()
