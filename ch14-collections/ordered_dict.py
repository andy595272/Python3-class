# 有序的dict  因為在舊的python版本可能不是按照給的順序給所以要使用

from collections import OrderedDict

# d = dict()
#
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# # 按照賦予職的順序{'a': 1, 'b': 2, 'c': 3}
# print(d)

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

print(d)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

d.move_to_end('a')  # 將指定的移到最後面

print(d)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])