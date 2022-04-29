# def add(a, b):
#     return a + b
#
# print(add(1, 2))
#
# def add1(a, b, c):
#     return a + b + c
#
# print(add1(1, 2, 3))

# def add(*args): # *args的使用
#     # print(args)
#     result = 0
#     for item in args:
#         result += item
#     return result
#
# print(add(1, 2, 15))

# def add(**kwargs): # **kwargs的使用 針對每個參數給值
#     # (a+b)*c
#     return (kwargs.get('a') + kwargs.get('b'))*kwargs.get('c')
#
# add(a = 1, b = 2, c = 3)

# def test(a, b, c):
#     print(a + b + c)
#
# def add(x, **kwargs):  # 透過**kwargs傳遞參數
#     if x == 2:
#         test(**kwargs)
#
# add(x=2, a=1, b=2, c=3)

def test(a, b=False):  # 默認值參數一定要在後面
    if b:
        return a
    else:
        return a * a

print(test(a=2, b=True))  # b 如果不帶參數 就是使用默認值


def test1(**kwargs): # 默認值一定要在最後
    pass