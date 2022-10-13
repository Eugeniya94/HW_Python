# Урок 4. Данные, функции и модули в Python. Продолжение
# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988

import decimal
num = decimal.Decimal(float(input('Введите число: ')))
num2=int(input('Введите количество цифр после запятой: '))
num3=round(num, num2)
print(num3)
