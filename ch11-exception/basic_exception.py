# 異常處理

a = [10, 4, 3, 7, 11, 6, 0, 9, 22]
try:
    b = [item for item in a if 100 % item == 0]
    print(b)
# except:
#     print('發生錯誤')  # 有發生錯誤會印出 並繼續完成後續結果

except ZeroDivisionError:  # 捕捉特定異常
    print('0不能作為除數')
except TypeError:   # 捕捉特定異常
    print('數據類型錯誤')
except Exception:   # 全部錯誤
    print('其他類型錯誤')

print('完成')