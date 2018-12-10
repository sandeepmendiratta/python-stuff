#!/usr/bin/env python

from __future__ import print_function, unicode_literals

my_ipaddress = ['192.168.1.1', '10.1.1.1', '172.16.31.254', '8.8.8.8', '8.8.4.4']
my_ipaddress.append(['10.10.10.10', '4.4.4.4'])
print(my_ipaddress)
my_ipaddress.extend(['20.20.20.20', '8.8.8.8'])
my_ipaddress = my_ipaddress + ['172.16.1.1', '172.16.1.2']
print(my_ipaddress[0])
print(my_ipaddress[-1])
