# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

list1 = []
for i in range(10):
    list1.append(randrange(1, 30))
print(list1)
len_list = len(list1)
for i in range(len_list):
    n1_list = randrange(len_list)
    n2_list = randrange(len_list)
    list1[n1_list], list1[n2_list] = list1[n2_list], list1[n1_list]
print(list1)