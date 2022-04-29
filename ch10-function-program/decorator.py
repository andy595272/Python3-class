# def test1(x):
#     print(test1.__name__)
#     return x * 2
#
# def test2(x):
#     return x * x * x
#
# test1(1)
# test2(2)

def test1(x):
    return x * 2

def test2(x):
    return x * x * x

def demo(f):
    def f_new(*args, **kwargs):  # 可以不限制帶入的參數數量
        print(f.__name__)
        return f(*args, **kwargs)
    return f_new

# f = demo (test1)
# print(f(2))

# f = demo(test2)
# print(f(2))

# @demo  # 可以在不影響原本的效果下 新增效果 就是裝飾器
# def test3(x):
#     return x * 2 * x
#
# a = test3(4)
#
# print(a)

@demo
def test3(x, y):
    print('hello world')

test3(1, 3)

def demo_new(s):
    def demo(f):
        def f_new(*args, **kwargs):
            print(f.__name__)
            print(s)
            return f(*args, **kwargs)

        return f_new
    return demo

@demo_new('hello')  #帶有參數的裝飾器
def test4(x,y,z):
    print('x={},y={},z={}'.format(x,y,z))

test4(1,2,3)



