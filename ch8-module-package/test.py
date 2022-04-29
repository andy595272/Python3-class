import sys

if '/Library/Frameworks/Python.framework/Versions/3.10/bin/python3' not in sys.path:
    sys.path.append('/Library/Frameworks/Python.framework/Versions/3.10/bin/python3')

from ch8.demo.math import my_sum

print(my_sum(1, 2, 3, 4))

# if __name__ == "__main__":  作為程式執行的入口
#     pass

