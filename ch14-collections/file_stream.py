# 假設現在是使用者

from demo.library import Base

# assert(hasattr(Base, 'read'))   # 判斷Base(父類)裡面有沒有read這麼屬性 跟下面if一樣意思

class FileStream(Base):

    def get(self):
        pass
    def write(self):
        pass

if __name__ == '__main__':

    f = FileStream()
    f.get()