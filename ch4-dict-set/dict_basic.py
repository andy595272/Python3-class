# 字典創建

a = {
    1: 'a',
    2: 'b',
    '3': 'c'
}

# 前面的是k 後面是value
# 不可改變的數據類型

l1 = [1, 2, 3]
t1 = (1, 2, 3)

c = {
    t1: l1
}

print(c)

d = dict()  # 字典創建
print(d)

e = dict(a=1, b=2, c='a')
print(e)

# 字典的訪問
print(e['a'])

e['d'] = 123
print(e)

e['c'] =3
print(e)
