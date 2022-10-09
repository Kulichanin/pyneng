# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    config_vlan_dict_access = {}
    config_vlan_dict_trunk = {}

    with open(config_filename, 'r') as file:
        a = [line.strip('\n') for line in file]
    for config_vlan in a:
        if 'interface FastEthernet' in config_vlan:
            vlan = config_vlan[10:]
        elif 'switchport access vlan' in config_vlan:
            config_vlan_access = config_vlan
            config_vlan_dict_access[vlan] = int(config_vlan_access[-2:])
        elif 'switchport trunk allowed vlan' in config_vlan:
            config_vlan_trunk = config_vlan
            cvl = [int(b) for b in config_vlan_trunk[31:].split(',')]
            config_vlan_dict_trunk[vlan] = cvl
    return config_vlan_dict_access, config_vlan_dict_trunk
