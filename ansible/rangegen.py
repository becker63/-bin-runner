#!/usr/bin/python
#range = input("enter address range: ")
from netaddr import IPNetwork
from collections import ChainMap
import os
import nmap
import collections
import flatdict

if os.path.exists("hosts"):
  os.remove("hosts")
else:
  print("file doesnt exist")

ips = []
chars = ["[sites]"]

file = open("hosts", "w")

nm = nmap.PortScanner()

for ip in IPNetwork("192.168.1.0/23"):
        ips.append(ip)
        writeable = str(ip)
        chars.append(writeable)

out = "\n".join(chars)
file.write(out)
file.close

connectrange = ['127.0.0.1','localhost']

def get_values(data):
    values = []
    for k, v in data.items():
        if isinstance(v, dict):
            values.extend(get_values(v))
        else:
            values.append(v)
    return values

nma = nmap.PortScannerAsync()
def callback_result(host, scan_result):
    print('------------------')
    #print(host,scan_result)
    a = get_values(scan_result)
    if('up') in str(a):
      print(host + " : up")
      x = str(host)
      connectrange.append(x)
      return connectrange
    else:
      print("down")

nma.scan('192.168.0.102-104','22', callback=callback_result)
while nma.still_scanning():
    nma.wait(1)

print(connectrange)
