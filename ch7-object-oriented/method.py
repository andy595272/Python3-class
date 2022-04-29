class People:

    def __init__(self, name, age): # 實例方法使用self
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi my name is {}, and I'm {}".format(
            self.name , self.age
        ))

    @classmethod   # 裝飾器 可以改變原有方法的行為
    def test1(cls):  # 類方法使用cls
        print('這是一個類方法')

    @staticmethod
    def test2(): # 靜態方法
        print("這是一個靜態方法")

p1 = People(name='Jack', age=20)
p1.sayhi()

p1.test1()
People.test1()

p1.test2()
People.test2()

