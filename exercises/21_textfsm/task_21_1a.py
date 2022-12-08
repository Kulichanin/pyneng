# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
"""
import textfsm


def parse_output_to_dict(template, command_output):
    with open(template) as temp:
        result_list = []
        
        parser = textfsm.TextFSM(temp)
        results = parser.ParseText(command_output)
        for result in results:
          result_list.append(dict(zip(parser.header, result))) 
        return result_list
