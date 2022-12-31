# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""
class IPAddress:
    def __init__(self, value):
        ip, mask = value.split('/')
        self._chek_ip(ip)
        self._chek_mask(mask)
        
    def __str__(self) -> str:
        return f"IP address {self.ip}/{self.mask}"

    def __repr__(self):
        return f"IPAddress('{self.ip}/{self.mask}')"
    
    def _chek_ip(self, ip):
        for i in ip.split('.'):
            if 0 <= int(i) <= 255 and len(ip.split('.')) == 4:
                self.ip = ip
            else:
                raise ValueError('Incorrect IPv4 address')

    def _chek_mask(self, mask):
        if 8 <= int(mask) <= 32:
            self.mask = int(mask)
        else:
            raise ValueError('Incorrect mask')


if __name__ == '__main__':
    ip1 = IPAddress('10.1.1.1/24')
    ip_list = []
    ip_list.append(ip1)
    print(ip_list)