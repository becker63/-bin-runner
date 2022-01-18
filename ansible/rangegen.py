#!/usr/bin/python
import os
import subprocess
import sys

import nmap
import pyfiglet
import ruamel.yaml

chars2 = ["[sites]"]
range = []

result = pyfiglet.figlet_format("NaoTercom")
print(result)

resp = input("all naos(1) or selection(2)?: ")

if resp == "2":
  char2 = ['[sites]']
  print("====================================================")
  var = input("list ips or hosts with a comma: ")
  print("")
  file = open("hosts", "w")
  var2 = var.split(',')

  for line in var2:
      var3 = char2.append(line)
     
  
  file.write('\n'.join(char2))
  print(char2)
  file.close

if resp == "1":

  if os.path.exists("hosts"):
    print("hosts already found")
  else:
    print("====================================================")
    input = input("enter range of nao subnet: ")
    
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

print("====================================================")
input("enter filename to send: ")
print("")

#import os

#subprocess.run('export ')
#c = os.environ.get('ANSIBLEPATH')
#print(c)
#inp = input("enter filename to send: ")
#ansiblepath = "/home/becker/nao-fun/ansible/" + inp
#os.environ['ANSIBLEPATH'] = ansiblepath
#print(c)
#path = '/home/becker/nao-fun/ansible/playbook.yml'
#def inplace_change(filename, old_string, new_string):
#    # Safely read the input filename using 'with'
#    with open(filename) as f:
#        s = f.read()
#        if old_string not in s:
#            print('"{old_string}" not found in {filename}.'.format(**locals()))
#            return
#
#    # Safely write the changed content, if found in the file
#    with open(filename, 'w') as f:
#        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
#        s = s.replace(old_string, new_string)
#        f.write(s)
#
#inplace_change(path, c, ansiblepath)
