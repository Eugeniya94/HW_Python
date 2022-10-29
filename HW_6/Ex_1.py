# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]
from random import sample

num = int(input())
def create_list(num: int):
    if num<0:
        return 'Error'
    nums_list = sample(range(1, num*2), num)
    return nums_list
num_list = create_list(num)
print(num_list)

# def more_num(nums_list: list):
#     sec_list = []
#     for i in range(1, len(nums_list)):
#         if nums_list[i] > nums_list[i-1]:
#             sec_list.append(nums_list[i])
#     return sec_list
# print(more_num(num_list))

def more_num(nums_list: list):
    sec_list = [nums_list[i] for i in range(1, len(nums_list)) if nums_list[i] > nums_list[i-1]]
    return sec_list
print(more_num(num_list))
