# 假設現在是維護者(維護這個父類) 強制用戶一定要實現的方法
from abc import ABCMeta, abstractclassmethod  #強制用戶一定要實現的方法

class Base(metaclass=ABCMeta):

    @abstractclassmethod  #強制用戶(子類)一定要實現的方法
    def read(self):
        # print('call read...')
        pass

    @abstractclassmethod #強制用戶(子類)一定要實現的方法
    def write(self):
        # print('call write...')
        pass