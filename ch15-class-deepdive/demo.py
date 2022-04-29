# Namespace 命名空間  訪問順序代表的命名的空間
# 有三種
#(1)built-in  提前內建的定義 dir(__builtins__)可以在終端查看
#(2)Global
#(3)Enclosing, local


# (1)built-in
# print(copyright)
# copyright = 'this is my copyright'  # 可以自己覆蓋掉原本的
#
# print(copyright)

# (2)Global
globals()  # 查看有哪些定義
globals()['y'] = 10  # 可以透過這種方式定義沒有的

# (3) Enclosing, local
c = 100  # Global的c

def foo(x, y):     # 相比於上面的這裡面的c是enclosing
    c = x + y
    print(f"c={c}")
    def bar():  # local 就是在enclosing裡面的定義的ｃ
        c = 200
        print(c)
    bar()

foo(10, 20)

print(f"c={c}")

