# -*- coding: utf-8 -*-

"""
Задание 23.3a

В этом задании надо сделать так, чтобы экземпляры класса Topology
были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
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

    def __add__(self, other):
        result_sum = list(self.topology.items()) + list(other.topology.items())
        return Topology(dict(result_sum))

    def __iter__ (self):
        print('__iter__')
        return iter(self.topology.items())

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
    t1 = Topology(topology_example)
    # pprint(t1)
    # pprint(t1.topology)
    for link in t1:
        print(link)