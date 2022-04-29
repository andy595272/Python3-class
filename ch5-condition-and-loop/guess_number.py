import random
a = random.randint(0, 100)
while True:
    num = int(input("請輸入一個0-100之間的數字:"))
    if num == a:
        print("猜對了")
        break
    elif num > a:
        print("猜大了,重新猜")
    else:
        print("猜小了,重新猜")