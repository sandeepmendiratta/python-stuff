#!/usr/bin/env python

from __future__ import print_function


''' compare if variable1 equals variable2
compare if variable1 is not equal to variable3 '''

ip_addr = "2001:db8:1234::1"
IP_ADDR = "2001:db8:1234::2"
ip_addr_1 = "2001:db8:1234::3"
print("")
print("Is variable1 equal to variable2: {}".format(ip_addr == IP_ADDR ))
print(" Is variable1 is not equal to variable3: {}".format(ip_addr != ip_addr_1))
