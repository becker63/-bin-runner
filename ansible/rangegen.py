#!/usr/bin/python
import os
import nmap

range = []

if os.path.exists("hosts"):
  print("host exists")
else:
  print("")
  print("")
  input = input("enter range of nao subnet: ")
  print("")
  print("")
  nmScan = nmap.PortScanner()

  nmScan.scan(input, '22')

  for host in nmScan.all_hosts():
    if nmScan[host].has_tcp(22) == True:
        range.append(host)

  ips = []
  chars = ["[sites]"]

  file = open("hosts", "w")

  nm = nmap.PortScanner()

  for ip in range:
        ips.append(ip)
        writeable = str(ip)
        chars.append(writeable)

  out = "\n".join(chars)
  file.write(out)
  file.close
