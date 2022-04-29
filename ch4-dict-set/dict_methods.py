d = {
    'Name': 'Jack',
    'Age': 9,
    'Grade': 5,
}

print(d['Name'])
print(d.get('Name'))

print(d.keys())  # 獲取全部資訊

print(d.values())  # 獲取字典裡面的值

print(d.items()) # 以括號形式返回

c = d.pop('Name') # pop取出值然後不放回

d.clear() # 清空字典

print(d)

# 字典的更新
c ={
    1: 1,
    2: 2
}

c[3] = 3
c[4] =4
print(c)

d = {
    1: 5,
    6: 6
}

# c.update(d)  # 更新值到字典裡  如果更新的key有衝突會覆蓋掉
# print(c)

e = {**c, **d} # 可以把字典合併形成新字典
print(e)