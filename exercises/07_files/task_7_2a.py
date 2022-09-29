# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

"""
with open('config_sw1.txt', 'r') as file:
    a = [line.strip('\n') for line in file]
    for i in a:
        if not (i.find(ignore[0]) != -1 or i.find(ignore[1]) != -1 or i.find(ignore[2]) != -1 or i.find('!') != -1):
            print(i)
"""
# Второй вариант более универсальный


ignore = ["duplex", "alias", "configuration"]


with open('config_sw1.txt', 'r') as f:
    for line in f:
        words = line.split()
        words_intersect = set(words) & set(ignore)
        if not line.startswith("!") and not words_intersect:
            print(line.rstrip())
