from collections import deque
# 雙向佇列 兩邊都可以操作

d = deque([1, 2, 3])

d.append(4) # 末尾增加
print(d) # [1, 2, 3, 4]
d.appendleft(0)  # 左邊插入數字
print(d) # [0, 1, 2, 3, 4]

d.pop() # 刪除末尾
print(d) # [0, 1, 2, 3]
d.popleft()  # 刪除左邊的
print(d) # [1, 2, 3]

d.extend([4, 5]) # 擴展
print(d) # [1, 2, 3, 4, 5]
d.extendleft([0, -1])  #左邊擴展 要注意順序、大小
print(d) # [-1, 0, 1, 2, 3, 4, 5]

d.reverse() # 反轉
print(d) # [5, 4, 3, 2, 1, 0, -1]

d.insert(0, 123)  # 傳入(index, 參數) 0是index
print(d) # [123, 5, 4, 3, 2, 1, 0, -1]