#!/usr/bin/env python

from __future__ import print_function

banner = "-" * 80
f = open("show_version.txt")
showver = f.read()
print("\n" + banner)
print(showver)
print(type(showver))
f.close
