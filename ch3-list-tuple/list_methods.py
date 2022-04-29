# 獲取列表的基本資訊

list1 = [9, 1, -4, 3, 7, 11, 3]

print('list的長度 ＝', len(list1))

print('list1里的最大值 ＝', max(list1))

print ('list1里的最小值 ＝', min(list1))

print ('list1里3這個元素一共出現了{}次'.format(list1.count(3)))

# 列表的改變

list2 = ['a', 'c', 'd']

# 給list2結尾添加一個新元素'e'

list2.append('e')
print('list2=', list2)

# 在 list2 的'a' 和 'c' 之間插入一個'b'

list2.insert(1, 'b')
print('list2= ', list2)

# 刪除list2里的b

list2.remove('b')
print('list2= ', list2)

# 列表翻轉

list3 = [1, 2, 3]
list3.reverse()
print('list3= ', list3)

# 列表排序

list4 = [9, 1, -4, 3, 7, 11, 3]
list4.sort(reverse = True) # 倒序 正序就空白
print('list4= ', list4)