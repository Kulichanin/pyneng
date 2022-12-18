# -*- coding: utf-8 -*-

"""
Задание 22.2b

Скопировать класс CiscoTelnet из задания 22.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного
режима и список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko
(пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_22_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

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
   
      if type(command) == list:
         self._write_line('conf t')
         self._telnet.read_until(b'#')
         for com in command:   
            com = self._write_line(com)
            output = self._telnet.read_until(b"#").decode('utf-8')
            return output.replace("\r\n", "\n")

      self._write_line(command)
      output = self._telnet.read_until(b"#").decode('utf-8')
      if parse:
         cli_table = clitable.CliTable(index, templates)
         cli_table.ParseCmd(output, attributes)
         return [dict(zip(cli_table.header, raw)) for raw in cli_table]
      return output.replace("\r\n", "\n")


if __name__ == '__main__':
  r1_params = {
  'ip': '192.168.100.1',
  'username': 'cisco',
  'password': 'cisco',
  'secret': 'cisco'}

  r1 = CiscoTelnet(**r1_params)
#   pprint(r1.send_show_command('sh ip int br'))
  pprint(r1.send_show_command(['interface loop55', 'ip address 5.5.5.5 255.255.255.255']))