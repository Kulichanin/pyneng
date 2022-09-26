# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input('Ввидите IP адрес:')
ip_address = ip_address.split('.')
try:
    for i in range(len(ip_address)):
        if int(ip_address[i]) > 255 or len(ip_address) != 4:
            a = 1 / 0
except (ValueError, ZeroDivisionError):
    print('Неправильный IP-адрес')
else:
    if 1 <= int(ip_address[0]) <= 223:
        print('unicast')
    elif 239 >= int(ip_address[0]) >= 224:
        print('multicast')
    elif ip_address == ['0', '0', '0', '0']:
        print('unassigned')
    elif ip_address == ['255', '255', '255', '255']:
        print('local broadcast')
    else:
        print('unused')