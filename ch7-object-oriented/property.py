class People:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def get_name(self):
    #     return self.__name

    @property
    def name(self):
        # 可以用來做格式的規範
        return self.__name.upper() # .upper()設定返回的都是大寫

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        # 做一些合法性的檢查
        self.__name = name

    # def set_names(self, name):
    #     return self.__age

    # def set_name(self, name):
    #     self.__name = name

    def set_age(self, age):
        self.__age = age

someone = People(name='Jack', age=20)
print(someone.name)
print(someone.age)
someone.name ='Test'
print(someone.name)