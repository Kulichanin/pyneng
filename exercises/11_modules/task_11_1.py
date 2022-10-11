# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    dictionary_show_cdp_neighbors = {}
    # Port_ID = []
    # Device_ID = []
    # Local_Intf = []
    # show_vlan_list = []
    for line in command_output.split('\n'):
        if 'show cdp neighbors' in line:
            show_vlan = line
            find_name_vlan = show_vlan.find('>')
            show_vlan = show_vlan[:find_name_vlan]
        elif 'Eth' in line:
            find_name_vlan_and_options = line.split()
            Device_ID = find_name_vlan_and_options[0]
            Local_Intf = find_name_vlan_and_options[1] + find_name_vlan_and_options[2]
            Port_ID = find_name_vlan_and_options[-2] + find_name_vlan_and_options[-1]
            dictionary_show_cdp_neighbors[(show_vlan, Local_Intf)] = (Device_ID, Port_ID)

    return dictionary_show_cdp_neighbors


if __name__ == "__main__":
    with open("sh_cdp_n_r3.txt") as f:
        print(parse_cdp_neighbors(f.read()))
