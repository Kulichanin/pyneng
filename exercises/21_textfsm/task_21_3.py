# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""

"""
Комментарий от себя для решения.
В command_output получаем вывод любой комманды cisco или иного производителя.
Используя attributes_dict, в котором имеется словарь с командой и вендором, находим по ключу 'Command' строку из файла index c именем шаблона.
применяем шалон из каталога templ_path для command_output.

"""

from textfsm import clitable
from pprint import pprint

def parse_command_dynamic(command_output, attributes_dict, index_file='index',templ_path='templates/'):
    results = []

    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    [results.append(dict(zip(list(cli_table.header),list(result)))) for result in cli_table]
    
    return results


if __name__ == '__main__':
  with open ('output/sh_ip_route_ospf.txt') as file:
    output = file.read()
  attributes = {'Command': 'show ip route ospf', 'Vendor':'cisco_ios'}
  pprint(parse_command_dynamic(output,attributes), width=100)