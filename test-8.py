#!/usr/bin/env python

from __future__ import print_function

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
mac1 = mac1.split()
mac2 = mac2.split()
mac3 = mac3.split()
ip_addr1 = mac1[1]
mac1 = mac1[3]
print()
print("{:20} {:20}".format("IP ADDR", "MAC ADDRESS"))
print("{:>20} {:>20}".format("-" * 20, "-" * 20))
print("{:>20} {:>20}".format(ip_addr1, mac1))
