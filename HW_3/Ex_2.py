# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]
from random import sample

def create_list(num:int):
    if num<0:
        return 'Error'
    num_list = sample(range(1, num*2), num)
    return num_list


def prod_num_list(num_list: list):
    new_list = []
    len_list = len(num_list)

    for i in range(len_list//2):
        prod_num = num_list[i]*num_list[len_list-i-1]
        new_list.append(prod_num)
    if len_list%2!=0:
        new_list.append(num_list[len_list//2])    
    return new_list
num = int(input('Введите число: '))
my_list = sample(range(1, num*2), num)
print(my_list,prod_num_list(my_list), sep='\n')            