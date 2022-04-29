# s = {1, 2, 3, 4}

# s.add(5)
# s.add(5) # 添加重複的會放棄 不會報錯

# print(s)

# s.remove(5)
# s.remove(5) # 刪除不存在的會報錯

# print(s)

# a = '12345123'

# s1 = set(a)

# print(s1)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1 & s2) # 交集
print(s1 | s2) # 全部的
print(s1 ^ s2) # 剔除兩邊都有的
print(s1 - s2)
print(s2 - s1)
