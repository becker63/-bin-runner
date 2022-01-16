#!/usr/bin/python
range = input("enter address range: ")
from netaddr import IPNetwork
import os

if os.path.exists("hosts"):
  os.remove("hosts")
else:
  print("file doesnt exist")

chars = ["[sites]"]

file = open("hosts", "w")

for ip in IPNetwork(range):
        writeable = str(ip)
        chars.append(writeable)

out = "\n".join(chars)
file.write(out)
file.close
