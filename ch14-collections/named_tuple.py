# 第一種方式 不直觀 需透過上下文判斷index是代表什麼
s1 = ('Richard', 33)
s2 = ('Chris', 24)

print(s1[0], s1[1])

# 第二種方式
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age =age

s1 = Student('Jack', 30)
s2 = Student('Tim', 20)

print(s1.name)
print(s2.age)

# 第三種方式
from  collections import namedtuple

Student = namedtuple('Student',['name', 'age'])

s3 = Student('Paul', 55)
s4 = Student('Nico', 40)

print(s3.name)
print(s4.age)
