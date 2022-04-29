word_list = ['is', 'who', 'when', 'it', 'is', 'who','is']

# result =dict()
# 計算每個詞出現的次數
# 第一種方法
# for word in word_list:
#     if word not in result:
#         result[word] = 1
#     else:
#         result[word] += 1
#
# print(result)

# #第二種方法
# for word in word_list:
#     result.setdefault(word, 0)  # 帶入一個k就是word 及一個預設值
#     result[word] += 1
# print(result)

# 第三種方法
from collections import defaultdict

result = defaultdict(int)  # 裡面參數是可調用的對象
for word in word_list:
    result[word] += 1

print(result)