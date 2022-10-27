# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель
# пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
# out
# The data is incorrect

from random import sample

def del_word(num, word):
    if num<0:
        print('Write incorrect number')
        return []
    list_of_words = []
    for i in range(num):
        words_str = ''.join(sample(word, 3))
        list_of_words.append(words_str)
    return ' '.join(list_of_words)



def rem_words(word: str) -> str:
    return ' '.join(word.replace('abc', '').split())

str_list = del_word(20, 'abc')
print(str_list)
print(rem_words(str_list))
