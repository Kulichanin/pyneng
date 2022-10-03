# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

value = input('Ввидите номер VLAN: ')
a = []
with open('CAM_table.txt', 'r') as file:
    [a.append(line.split()) for line in file if 'DYNAMIC' in line]
    [print('{:10}{:20}{:10}'.format(a[i][0], a[i][1], a[i][3])) for i in range(len(a)) if a[i][0] == value]