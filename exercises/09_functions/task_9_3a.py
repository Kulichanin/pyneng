# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

access_port_vlan_1 = ['interface FastEthernet', 'switchport mode access', 'duplex auto']

def get_int_vlan_map(config_filename):
    config_vlan_dict_access = {}
    config_vlan_dict_trunk = {}

    with open(config_filename, 'r') as file:
        a = [line.strip('\n') for line in file]
    for config_vlan in range(len(a)):
        if 'interface FastEthernet' in a[config_vlan] and 'switchport mode access' in a[config_vlan+1] and 'duplex auto' in a[config_vlan+2]:
            config_vlan_name = a[config_vlan]
            config_vlan_dict_access[config_vlan_name[10:]] = 1
        elif 'interface FastEthernet' in a[config_vlan]:
            vlan = a[config_vlan][10:]
        elif 'switchport access vlan' in a[config_vlan]:
            config_vlan_access = a[config_vlan]
            config_vlan_dict_access[vlan] = int(config_vlan_access[-2:])
        elif 'switchport trunk allowed vlan' in a[config_vlan]:
            config_vlan_trunk = a[config_vlan]
            cvl = [int(b) for b in config_vlan_trunk[31:].split(',')]
            config_vlan_dict_trunk[vlan] = cvl


    return config_vlan_dict_access, config_vlan_dict_trunk

print(get_int_vlan_map('config_sw2.txt'))