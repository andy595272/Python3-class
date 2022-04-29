# counter 統計相關工作使用 ex 統計字詞

from collections import Counter

word_list = ['is', 'who', 'when', 'it', 'is', 'who', 'is']

# c = Counter(word_list)   # 可以帶參數 也可以自行輸入 例如'ndfnaifnoafnaio'
# print(c)

c = Counter('dmsfidsnfsf')
# print(c.most_common(3)) # 可以算出常出現的前3名 [('s', 3)(字母, 次數)]

print(c)

c.update('fosnfisfons')  # 更新並進行統計
print(c)





