# pdb debug

# import pdb
# pdb.set_trace()
# 上面兩行用來debug用 找到後記得刪除！！
# 可以打？看列表  s 一步一步運算

numbers = [1, 2, 3, 4]

def all_even(num_list):

    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)

    return even_numbers

a = all_even(numbers)

print(a)

b = input('please input')

print(b)