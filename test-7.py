#!/usr/bin/env python

from __future__ import print_function


''' 4. Create a show_version variable that contains the following

 show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

Remove all leading and trailing whitespace from the string.

Split the string and extract the model and serial_number from it.

Check if 'Cisco' is contained in the model string (ignore capitalization).

Check if '881' is in the model string.

Print out both the serial number and the model.

'''
show_version =  "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.split()
model = show_version[1]
version = show_version[2]
print("")
print(show_version)
vendor = "cisco" in model.lower()
print("Checking if model contains Cisco: {}".format(vendor))
ver = '881' in model.lower()
print("checking serial in serial number {}".format(ver))
