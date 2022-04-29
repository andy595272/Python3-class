# 繼承
class Animals:

    def eat(self):
        print('Animal is eating')

class Bird(Animals):

    def sing(self):
        print('Bird is singing......')

    def eat(self):
        print('Bird is eating.....')

class Dog(Animals):

    def eat(self):
        print('Dog is eating......')
#
a = Animals()
# a.eat()
#
b = Bird()
# b.eat()
#
d = Dog()
# d.eat()

def  demo_eat(a):
    a.eat()

for item in [a, b, d]:
    demo_eat(item)

# isinstance 用來判斷type類型 ！！！