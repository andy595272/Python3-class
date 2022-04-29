# __init__
# __repr__
# 雙下滑線的方法稱為double underscore = dunder =magic_method

class Account:

    def __init__(self, name, amount=0):
        self.name = name
        self.amount =amount
        self._transaction = []

    @property  # 作用class的屬性 不用再帶函數 print(a.balance)
    # 沒有property就是print(a.balance())
    def balance(self):
        return self.amount + sum(self._transaction)

    def __len__(self):   # 這是magic method
        return len(self._transaction)
    def __repr__(self):  # 用於程序比較精確使用  = 意思等同於__str__
        return f'Account({self.name}, {self.amount})'
    # def __str__(self):  # 用於人類讀取使用 比較好看
    #     return f'name={self.name}, amount = {self.amount}'

    def add_transaction(self, amount):
        self._transaction.append(amount)

    def __eq__(self, other):  # 判斷是否相等 返回true/false
        return self.balance == other.balance

    def __lt__(self, other):  # 判斷是否小於
        return self.balance < other.balance

a1 = Account('Jack', 10)
a1.add_transaction(100)
a1.add_transaction(-20)

a2 = Account('Mark', 10)
a2.add_transaction(200)
a2.add_transaction(-50)
a2.add_transaction(10)

print(a1==a2)  # __eq__使用
print(a1<a2)  # __lt__使用

print(len(a1))   # __len__使用
print(a1.balance)  # 求值 創建出新的def balance   __repr__使用