# f = open("test3.txt", mode='x') # 生成文件
#
# f.write("line 1\n")
#
# f.writelines(["line 2\n", "line 3\n"]) # 往文件內寫內容
#
# f.close()

f = open("test5.txt", mode='w', encoding='utf8')
# 為了寫入中文 要加encoding
f.write("第一行\n")
f.close()