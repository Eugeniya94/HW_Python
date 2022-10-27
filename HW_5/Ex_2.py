# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.
#
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from itertools import groupby, starmap
from os import path


def rle_file(text='text_words.txt', text2='text_code_words.txt'):
    if path.exists(text) and path.exists(text2):
        with open(text) as my_f, \
                open(text2, 'a') as new_f:
            for i in my_f:
                # new_f.write(''.join([f'{len(list(v))}{ch}'for ch, v, in groupby(i)]))
                for ch, v, in groupby(i):
                    new_f.write(''.join([f'{len(list(v))}{ch}']))
    else:
        print('Файла нет в системе')


def rle_file_decode(file):
    if path.exists(file):
        with open(file) as f:
            st = ''
            for k in f:
                num = []
                for i in k.strip():
                    if i.isdigit():
                        st += i
                    else:
                        num.append([int(st), i])
                        st = ''
                print(''.join(starmap(lambda x, y: x * y, num)))
    else:
        print('Файла нет в системе')


rle_file(input('Введите название файла с текстом: '), input('Ведите название файла для изменений: '))
rle_file_decode(input('Введите название файла для декодирования: '))
