import os
from pathlib import Path

# in_file = os.path.join(os.getcwd(), "demo", "text.txt")
# # join 結合路徑
# print(in_file)
#
# a = Path.cwd()
#
# print(a)
#
# print(type(a))

p = Path.cwd().parent #當前目錄
for file in p.rglob('*.txt'): # rglob具有篩選包含有.txt的文件
    print(file)

# glob,rglob 查找目錄  會根據篩選條件印出