# 2. Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.
# Простые делители числа

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]
num = int(input(':'))

def simple_nums_list(num):
    x = 2
    fact_num = []
    if num<0:
        return 'Error'
    while num>1:
        if num%x == 0:
            fact_num.append(x)
            num//=x
        else:
            x+=1
    return fact_num
print(simple_nums_list(num))                
        
