# 類的定義

class Myclass:
    pass

# _init_() method 方法 function(函數)
# attribute 屬性
# method 方法

class people:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))

# class instance 類的實例

someone = people(name='Jack', age=20)
print(someone.name)
print(someone.age)
someone.sayhi()
