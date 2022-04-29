# deque 跟 list比較

from  collections import deque
import time

d = deque(range(10000000))
# print(d)

l = list(range(10000000))
# print(l)

t1 = time.time()
# d.append(-1)
print(d[599999])
# d.insert(1110, -1)
print('deque:', time.time() -t1)

t2 = time.time()
# l.append(-1)
print(l[599999])
# l.insert(1110, -1)
print('list:', time.time() -t2)

# append 時 list 效率更好
# insert 時 deque 更好,  因為其他的位置需要更動