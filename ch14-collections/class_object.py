class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'name={self.name}, age={self.age}'

s1 = Student(name='test', age=10)
l1 = [1, 2, 3]
d1 = {
    1:1,
    2:2
}