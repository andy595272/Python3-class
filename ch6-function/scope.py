# x = 1
# x += 1
#
# print(x)
#
# def demo():
#     x = 10
#     print(x)
#
# demo()
#
# print(x)

# y = [1, 2, 3]
# print(y)
#
# def demo1(a):
#     a.append(4)
#     print(a)
#
# demo1(a=y)
#
# print(y)

z = 1
print(z)
def demo2(a):
    global z  # 設定z為global 全局變數可以改變
    z = z + a
    print(z)

demo2(a=10)

print(z)