# 集合

a = {'a', 'b', 'c'}

b = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(type(a))

t = 'a' in a  # boolean類型 判斷值有沒有在集合內
print(t)

x = 'a' in b
print(x)

l = [1, 2, 3, 2, 4, 5, 2]
s1 = set(l)  # 集合創建
print(s1, type(s1), list(s1))

