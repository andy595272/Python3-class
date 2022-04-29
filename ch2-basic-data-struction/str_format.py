name = "python"
age = 25

# 要印出來 "我是python, 今年25歲"

# 第一種方法
new_str = "我是" + name + "," + "今年" + str(age) + "歲"
print(new_str)

# 第二種方法 在python 2使用
new_str_1 = "我是%s, 今年%d歲" % (name,age)
print(new_str_1)

# 第三種方法 在python 3使用
new_str_2 = "我是{name}, 今年{age}歲".format(name = 'aaa', age = 'bbb')
print(new_str_2)

# 最新的一種 最推薦！！！
name1 = "andy"
age1 = 27
new_str_3 = f"我是{name1}, 今年{age1}歲"
print(new_str_3)