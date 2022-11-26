# -*- coding: utf-8 -*-
"""
Задание 19.2

Создать функцию send_show_command_to_devices, которая отправляет одну и ту же
команду show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя текстового файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в обычный текстовый файл в таком формате
(перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
"""
from concurrent.futures import ThreadPoolExecutor
from yaml import safe_load
from netmiko import ConnectHandler

import logging

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
    # format='%(threadName) s%(name)s %(levelname)s: %(massage)s', # узнать как тут чего! Эксперименты
    level=logging.INFO,
    )


def send_show_commmand(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        name_device = ssh.find_prompt()
        result = ssh.send_command(command)
        return name_device, result

def send_show_command_to_devices(devices, command, filename, limit=3):

    with ThreadPoolExecutor(max_workers=limit) as executor:
        with open(f'{filename}', 'w') as file:    
            for device in devices:
                request = executor.submit(send_show_commmand, device, command)
                logging.info(request.result())
                file.write(f'{request.result()[0]}{command}\n')
                file.writelines(f'{request.result()[1]}\n')


"""if __name__== '__main__':
    with open('/home/kdv/pyneng/exercises/19_concurrent_connections/devices.yaml') as file:
        devices = safe_load(file)
    send_show_command_to_devices(devices, 'sh ip int br', "test.txt")"""
