# -*- coding: utf-8 -*-
"""
Задание 19.3

Создать функцию send_command_to_devices, которая отправляет разные
команды show на разные устройства в параллельных потоках, а затем записывает
вывод команд в файл. Вывод с устройств в файле может быть в любом порядке.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять
  какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом
команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh int desc
Interface                      Status         Protocol Description
Et0/0                          up             up
Et0/1                          up             up
Et0/2                          admin down     down
Et0/3                          admin down     down
Lo9                            up             up
Lo19                           up             up
R3#sh run | s ^router ospf
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
"""

# Этот словарь нужен только для проверки работа кода, в нем можно менять IP-адреса
# тест берет адреса из файла devices.yaml
commands = {
    "192.168.100.3": "sh run | s ^router ospf",
    "192.168.100.1": "sh ip int br",
    "192.168.100.2": "sh int desc",
}

from concurrent.futures import ThreadPoolExecutor, as_completed
from yaml import safe_load
from netmiko import ConnectHandler

import logging

logging.getLogger('paramiko').setLevel(logging.WARNING)

logging.basicConfig(
  level=logging.INFO,
)


def send_show_command(device, command):
  with ConnectHandler(**device) as ssh:
    ssh.enable()
    name_device = ssh.find_prompt()
    result = ssh.send_command(command)
  return name_device, result

def send_command_to_devices(devices, commands_dict, filename, limit=3):
  with ThreadPoolExecutor(max_workers=limit) as executor:
    with open(filename, 'w') as file:
      for ip, command in zip(commands_dict.keys(), commands_dict.values()):
        for device in devices:
          if device['host'] == ip:
            request = executor.submit(send_show_command, device, command)
            logging.info(request.result())
            file.write(f'{request.result()[0]}{command}\n')
            file.writelines(f'{request.result()[1]}\n')

if __name__== '__main__':
    with open('/home/kdv/pyneng/exercises/19_concurrent_connections/devices.yaml') as file:
        devices = safe_load(file)
    send_command_to_devices(devices, commands, "/home/kdv/pyneng/exercises/19_concurrent_connections/test_19_3.txt")