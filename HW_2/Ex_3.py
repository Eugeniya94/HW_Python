# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


num = int(input('Введите число: '))
sum = 0
list = []
for i in range(1,num + 1):
    res = round((1 + 1/i) ** i)
    list.append(res)
    sum+=res
print(f'{list} -> {sum}')


