# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

"""
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
"""

while True:
    ip_address = input('Введите IP адрес:')
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
        break
