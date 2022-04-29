# 測試---單元測試

def add(a, b):
    """
    >>> add(1, 2)
    3
    >>> add(1, 1.2)
    Traceback (most recent call last):
    ValueError : a和b必須是整數
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("a和b必須是整數")

if __name__ == '__main__':
    import doctest
    doctest.testmod()