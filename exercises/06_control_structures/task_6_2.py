# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input('Ввидите IP адрес:')
ip_address = ip_address.split('.')
if 1 <= int(ip_address[0]) <= 223:
    print('unicast')
elif 239 >= int(ip_address[0]) >= 224:
    print('multicast')
elif ip_address == ['0','0','0','0']:
    print('unassigned')
elif ip_address == ['255','255','255','255']:
    print('local broadcast')
else:
    print('unused')
