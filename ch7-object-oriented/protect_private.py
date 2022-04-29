class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._protect_var = 10  # _protect可以保護但仍然可以修改
        self.__private_var = 10 # 受保護的 只能在class裡面使用

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))

    def get_var(self):
        print(self.__private_var)

    def set_var(self, var):
        self.__private_var = var


someone = People(name='Jack', age=20)
# someone.sayhi()
# someone.age = 30
# someone.sayhi()
# someone._protect_var = 30

