# 通過print語句找出錯誤

numbers = [1, 2, 3, 4, 10, -4, -7, 0]

def all_even(num_list):

    even_numbers = []
    for number in num_list:
        print('number=', number)
        if number % 2 == 0:
            print('發現偶數, number=', number)
            even_numbers.extend([number])
        # 將number改成列表 加上[]
    return even_numbers

print('all even number', all_even(numbers))