# 測試---文檔測試
# 適合用於小型的檔案 只有簡單函數或幾個類別
# 在註釋裡面去寫運算及結果 去驗證看看是否正確
def func_demo(a, b):
    """ doc test demo
    >>> func_demo(1, 2)
    3
    >>> func_demo('a', 'b')
    'ab'
    >>> func_demo([1, 2],[3, 4])
    [1, 2, 3, 4]
    >>> func_demo({1:1},{2:2})
    False
    >>> func_demo(1, '2')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>
    """
    if isinstance(a, dict):
        return False
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()