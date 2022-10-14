# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]
from itertools import count
from random import randrange
num = int(input('Введите количество чисел: '))
def numbers(num: int):
    num_list = []
    if num<0:
        print('Incorrectly number')
        return []
    for i in range(1, num+1):
        num_list.append(randrange(0, num+1))
    return num_list    

    

def origin_nums(num_list: list):
    end_list = []
    for i in num_list:
          if num_list.count(i)==1:
            end_list.append(i)
    return end_list 
n_list = numbers(num)    
print(n_list, origin_nums(n_list), sep='\n')



