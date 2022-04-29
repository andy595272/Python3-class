# lambda匿名函數

def test(x, y):
    return x + 2 * y

# f = lambda x, y: x + 2 * y
# 達到快速定義
print(test(1, 2))

# print(f(1, 2))

def demo(x, y, f):
    return f(x, y)

print(demo(1, 2, lambda x, y: x + 2 * y))

def add_n(n):
    return lambda x: n + x

f = add_n(40)  # f是函數 傳入參數去獲取結果
print(f(1))
print(f(-10))