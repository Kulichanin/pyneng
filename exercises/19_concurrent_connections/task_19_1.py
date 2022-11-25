# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
from concurrent.futures import ThreadPoolExecutor
from os import system

import logging

logging.basicConfig(
    format='%(threadName)s%(name)s%(levelname)s%(massage)s',
    level=logging.INFO
)
def ping_ip_address(ip):
    response = system(f'ping -c 1 {ip}')
    return response

def ping_ip_addresses(ip_list, limit=3):
    available = []
    not_available = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip_address, ip_list)
        for value,ip in zip(result, ip_list):
            logging.info(f'___________{value}_____________')
            match value:
                case 0: available.append(ip)
                case _: not_available.append(ip)
    return (available, not_available)