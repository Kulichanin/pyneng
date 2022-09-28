# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
param = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

with open('ospf.txt', 'r') as f:
    text = [line.split() for line in f]
for i in text:
    print('{:20} {:20}'.format(param[0], i[1]))
    print('{:20} {:20}'.format(param[1], i[2].strip('[]')))
    print('{:20} {:20}'.format(param[2], i[4].rstrip(',')))
    print('{:20} {:20}'.format(param[3], i[5].rstrip(',')))
    print('{:20} {:20}'.format(param[4], i[6]))

