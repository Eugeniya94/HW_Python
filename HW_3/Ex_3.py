# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

num = int(input('Введите число: '))
num_list = []

def bin_num(num:int):
    if num<0:
        print('Вы ввели неверное число')
        return 0

    while num!=0:
        n = num%2
        num_list.append(n)
        num//=2
    return num_list
    
n_list = bin_num(num)

def rev_string(num_list:list):
    new_list = ''.join(str(i) for i in num_list)
    rev_list = ''.join(reversed(new_list))
    return rev_list

print(rev_string(n_list))
print(type(rev_string(n_list)))

  
    


