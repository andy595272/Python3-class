f = open('test5.txt', encoding='utf8') # open 要保證文件存在

# for line in f :
#     print(line)

# a = f.readline() #循環取值 只能讀一次 可透過seek回到頭
# b = f.readlines() # 不推薦
#
# print(a,type(a))
# print(b,type(b))

for line in f:
    print(line)

for line in f:
    print(line)
f.close()