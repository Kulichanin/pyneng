# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Соединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Соединение с одним из портов существует


"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

from pprint import pprint


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        for key in list(topology_dict.keys()):
            for value in list(topology_dict.values()):
                if value == key: topology_dict.pop(value)
        return topology_dict

    def delete_link(self, *delete_link):
        if self.topology.get(delete_link[0]) != None:
            self.topology.pop(delete_link[0])
        elif self.topology.get(delete_link[1]) != None:
            self.topology.pop(delete_link[1])
        else:
            print("Такого соединения нет")
    
    def delete_node(self, name_node):
        dict_copy = self.topology.copy()
        for i,j in self.topology.items():
            if name_node in j:
                dict_copy.pop(i)
        if self.topology == dict_copy:
            print('Такого устройства нет')
        else:
            self.topology = dict_copy
    
    def add_link(self,*link):
        if (self.topology.get(link[0]) != None) and (link[1] in self.topology.values()):
            print('Такое соединение существует')
        elif (self.topology.get(link[0]) != None) or (link[1] in self.topology.values()):
            print('Соединение с одним из портов существует')
        else:
            self.topology[link[0]] = link[1]


if __name__ == "__main__":
    top1 = Topology(topology_example)
    # pprint(top1.topology)
    top1.add_link(('R5', 'Eth0/1'), ('SW2', 'Eth0/11'))
    pprint(top1.topology)