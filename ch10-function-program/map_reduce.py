a = [1, 2, 3, 4]

# def f(x, y)
#    return x + y

# print(map(lambda x: x * x, a))

# for item in map(lambda x: x * x, a):
#     print(item)

# print([item for item in map(lambda x: x * x, a)])

# from functools import reduce
#
# a = reduce(lambda x, y: x + y, a)
# print(a)

# a = filter(lambda x:x % 2 == 1,a)
# print(a)

print([item for item in a if item % 2 == 1])