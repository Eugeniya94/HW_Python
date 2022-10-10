# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36
from random import uniform
num = int(input())
float_list = []
def float_num_list(num: int):
    if num<0:
        return 'Вы ввели отрицательное число'
    for i in range(num):
       float_list.append(round(uniform(1, num), 2))
    return float_list    
def max_min_num(float_list: list):
    num_max = float_list[0]%1
    num_min = float_list[0]%1
    for i in range(1, len(float_list)):
         number = round(float_list[i]%1, 2)
         if number>num_max:
            num_max = number
         elif number<num_min:
            num_min = number
    result = round((num_max - num_min), 2)
    print(f'Max = {num_max}, Min = {num_min}, Diff = {result} ')  
    return result      

num_list = float_num_list(num)
print(num_list, max_min_num(num_list), sep='\n')