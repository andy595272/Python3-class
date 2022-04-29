# 列表解析
# 用列表數據快速生成另外一個列表

a = [1, 2, 3, 4]
# 假設要生成新列表 b = [2, 3, 4, 5]

# b = [item for item in a]  # 取出一個放一個 可以在前面進行運算
b = [item+1 for item in a if item % 2 ==0] # 可以加if判斷
print(b)

# 字典解析 快速生成一個字典
# python 內建高階函數 map, reduce

