# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

pos_num1 = int(input(':'))
pos_num2 = int(input(':'))
n = int(input(':'))
list = []
for i in range(-n, n + 1):
    list.append(i)
print(list)
if pos_num1 > ((n ** 2) + 1) or pos_num2 > ((n ** 2) + 1):
    print(False)
else:
    a = list[pos_num1 - 1]
    b = list[pos_num2 - 1]
print(a * b)