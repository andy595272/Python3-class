# 用戶自訂義異常

class MyException(Exception):
    pass

# raise MyException("這是用戶定義的異常")   # raise 觸發異常

try:
    raise MyException("這是用戶定義的異常")
except MyException as e:
    print(e)

# assert 斷言 可以觸發異常的方式

def my_interaction():
    raise  MyException('用戶自訂義的異常')
try:
    my_interaction()
except MyException as error:
    print(error)
else:  # 沒有發生except時會執行
    try:  # 使用with語句宣告 不用在後面close檔案
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:  #   不管有沒有異常都會執行
    print('清理工作')



