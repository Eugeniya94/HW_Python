# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
#  (или на какой оси она находится).
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координату X '))
y = int(input('Введите координату Y '))

if x > 0 and y > 0:
        a = 1
elif x < 0 and y > 0:
        a = 2
elif x < 0 and y < 0:
        a = 3
elif x > 0 and y < 0:
        a = 4        
print(f"Точка находится в четверти {a}")