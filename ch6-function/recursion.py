# n! = 1*2*3.......(n-1)*n

# n * (n-1)* (n-2)......* 2 * 1

# def test(n):   for迴圈做法
#     result = 1
#     for item in range(1, n+1):
#         result = result * item
#     return result
#
# print(test(5))

def test(n):  # 用遞歸的做法 更加簡單
    if n == 1 :
        return n
    return n * test(n-1)


print(test(7))