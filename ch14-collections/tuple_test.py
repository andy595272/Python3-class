# tuple 元組

print('1.iterable') # 便利的 可以打印出每一個元素
my_tuple = ('pyhton', 3, 7, 3)
for i in my_tuple:
    print(i)

print('2.indexing and slicing')  # 索引跟切片 透過索引訪問元素
print(my_tuple[0])
print(my_tuple[0:2])  # 訪問0-2就是0,1兩個

print('3.sequence unpacking') # 序列解包
name, _, y, z = my_tuple
print(name, y, z)  # 結果 python, y=7, x=3 不重要的用下底線

name, *_ = my_tuple  # 代表只關心第一個 後面後*_ 帶掉
print(name)

name, *version = my_tuple  # 將後面的元素付給同一個使用＊參數
print(name, version)   # version 會變成一個列表

print('4.immutable')  # 元組值是不可以變的
# my_tuple[1] = 2  是不可以這樣操作的 只能透過新生成一個

my_dict = {my_tuple: 1}
print(my_dict)

# my_dict = {[1, 2]: 1} 不可以這樣做 要作為字典的必須immutable

i = 1
a = {i: 1}
i = 2   # 這裡的i等於是重新的一個跟上面那個不一樣 所以a 的i不會變
print(a)