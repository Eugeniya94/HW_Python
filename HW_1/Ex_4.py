# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

quarter = int(input('Введите номер четверти: '))

if quarter == 1:
    print('x > 0 and у > 0')
elif quarter == 2:
    print('x < 0 and y > 0')
elif quarter == 3:
    print('x < 0 and y < 0 ')
elif quarter == 4:
    print('x > 0 and y < 0')
else:
    print('Вы ввели неверное число')