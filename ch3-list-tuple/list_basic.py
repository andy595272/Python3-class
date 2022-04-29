a = [1, 2, 3]
b = [1, 'abc', 2.0, ['a','b','c']]

print(a)
print(b)

print(a[0], a[1], a[2], sep='-')  # sep 代表用什麼區隔  end代表用什麼結尾

c = b[1:3]  # 印出從b[1]開始 往後數3-1個
print(c, type(c))

s = 'abcabc'
print(s[1:3], s[-1])
print(b[-1])