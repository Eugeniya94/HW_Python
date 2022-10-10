# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8
from random import sample

num = int(input('Введите количество чисел: '))

def random_list(num: int):
    if num<0:
        return 'Неверное число'

    rand_list = sample(range(1, num*2), num)
    return rand_list        


def sum_num_list(rand_list: list):
    neg_sum = 0
    for i in range(0, len(rand_list), 2):
        neg_sum += rand_list[i]
    return neg_sum


my_list = random_list(num)
print(my_list, sum_num_list(my_list), sep='\n')


   




