# 完善裝飾器
import functools

def demo(f):

    @functools.wraps(f) #
    # 用來複製屬性 放在裝飾器外 將f(0)的屬性到f_new裡面
    # 為了讓屬性保持不變
    def f_new(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return f_new

@demo
def test1(x, y):
    """
    this is test1
    :param x:
    :param y:
    :return:
    """
    print('x={},y={}'.format(x,y))

print(test1.__name__)
print(test1.__doc__)