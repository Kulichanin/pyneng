# -*- coding: utf-8 -*-

"""
Задание 22.2a

Скопировать класс CiscoTelnet из задания 22.2 и изменить
метод send_show_command добавив три параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей,
  полученный после обработки с помощью TextFSM.
  При parse=True должен возвращаться список словарей, а parse=False обычный вывод.
  Значение по умолчанию - True.
* templates - путь к каталогу с шаблонами. Значение по умолчанию - "templates"
* index - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"


Пример создания экземпляра класса:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_22_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:
In [4]: r1.send_show_command("sh ip int br", parse=True)
Out[4]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'}]

In [5]: r1.send_show_command("sh ip int br", parse=False)
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status
Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up
up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up...'


"""
import telnetlib
import time

from textfsm import clitable
from pprint import pprint

class CiscoTelnet:
  def __init__(self, ip, username, password, secret):
    self.ip = ip

    self._telnet = telnetlib.Telnet(ip)
    self._telnet.read_until(b'Username:')
    self._write_line(username)
    self._telnet.read_until(b'Password:')
    self._write_line(password)
    self._telnet.write(b'enable\n')
    self._telnet.read_until(b'Password:')
    self._write_line(secret)
    time.sleep(0.5)
    self._telnet.read_very_eager()

  def _write_line(self, line):
    return self._telnet.write(line.encode('utf-8') + b'\n')

  def send_show_command(self, command, parse=True,templates="/home/kdv/pyneng/exercises/22_oop_basics/templates",index="index"):
    attributes = {"Command": command, "Vendor": 'cisco_ios'}
    
    self._write_line(command)
    output = self._telnet.read_until(b"#").decode('utf-8')
    if parse:
      cli_table = clitable.CliTable(index, templates)
      cli_table.ParseCmd(output, attributes)
      return [dict(zip(cli_table.header, row)) for row in cli_table] 
    return output.replace("\r\n", "\n")


if __name__ == '__main__':
  r1_params = {
  'ip': '192.168.100.1',
  'username': 'cisco',
  'password': 'cisco',
  'secret': 'cisco'}

  r1 = CiscoTelnet(**r1_params)
  pprint(r1.send_show_command('sh ip int br'))