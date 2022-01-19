#!/usr/bin/python
import os
import subprocess
import sys
import nmap
import pyfiglet
import ruamel.yaml
import time
from termcolor import colored
from pyfiglet import Figlet

chars2 = ["[sites]"]
range = []

def rangegen():
  print("")
  print("")
  scanin = input("all naos(1) or selection(2): ")
  
  if scanin == "2":
    char2 = ['[sites]']
    print("====================================================")
    var = input("list ips or hosts with a comma: ")
    print("")
    file = open("hosts", "w")
    var2 = var.split(',')

    for line in var2:
        var3 = char2.append(line)


    file.write('\n'.join(char2))

    file.close

  if scanin == "1":

    if os.path.exists("hosts"):
      print("hosts already found")
    else:
      print("====================================================")
      rangein = input("enter range of nao subnet: ")

      nmScan = nmap.PortScanner()

      nmScan.scan(rangein, '22', )

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
      print(ips)

def run():
  print("")
  print("")
  with open('hosts', 'r') as file:
    data = file.read()
    runfile = "sudo bash -c 'cd /home/becker/nao/naoqi/pynaoqi && python2 /home/becker/nao-fun/ansible/naomain.py"
    data2 = str(data).replace('[sites]', '')
    data3 = data2.splitlines()
    del data3[0]
    print("====================================================")
    print("")
    for ip in data3:
      runfile2 =runfile +' ' + ip + "'" #+  ' > ' +'/home/becker/nao-fun/ansible/errors/'+ ip + '.txt' " && disown'"
      try:
        a = subprocess.check_output(runfile2, shell=True)
        print(a)
      except subprocess.CalledProcessError as e:
        print(e.output)
      print("")
      print("====================================================")
      print("")

f = Figlet(font='ogre', width=75)
print(colored(f.renderText('NaoTercom'), 'red'))


intro = input("scan(1) or run(2):")
if intro == "1":
  rangegen()
elif intro == "2":
  run()
