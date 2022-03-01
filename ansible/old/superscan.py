import subprocess
import time
import os
import colorama
from colorama import Fore, Back, Style
from termcolor import colored
print(Fore.RED + Back.BLACK +'\n fuck it. we are doing EVERY subnet. \n' + Style.RESET_ALL)
minp = input("enter min parallelism (defualt 1000): ")
maxp = input("enter max parallelism (defualt 1300): ")
print(colored("\n enter substrings to search for in hostname. \n", 'green'))
search1 = input("substring (1): ")
search2 = input("substring (2): ")
search3 = input("substring (3): ")
search4 = input("substring (4): ")

print(colored("\n enter number of subnets to search (max and defualt 255). \n", 'green'))
subnetstosearch = input("subnets: ")
if subnetstosearch == "":
    subnetstosearch2 = 255
else:
    subnetstosearch2 = int(subnetstosearch)

print(colored("\n enter number of hosts to search (max and defualt 255). \n", 'green'))
host = input("hosts: ")
if host == "":
    hosts = 255
else:
    hosts = host


if minp == "":
    minpi = 1000
else:
    minpi = int(minp)
if maxp == "":
    maxpi = 1300
else:
    maxpi = int(maxp)

out = []

rows, columns = os.popen('stty size', 'r').read().split()
check = f'time nmap -sP --min-parallelism={minpi} --max-parallelism={maxpi} 192.168.'
check2 = '192.168.'
i = 0
while i < subnetstosearch2 + 1:
  print(colored("\n" + str(i) + "\n", 'yellow'))
  row = '=' * int(rows)
  print(row)
  scan = check + str(i) + ".0-" + str(hosts)
  time.sleep(0)
  print("\n" + scan + "\n")
  a = subprocess.check_output(scan, shell=True).decode('ascii')
  print("")
  print(a)
  out.append(a)
  i += 1
print("")
row2 = "\n\n\n\n" + row + "\n\n\n\n"
fullout = row2.join(out)
print("")
print("")
a = fullout.splitlines()

print("")
print("")
print("")
import re
#a = ['Starting Nmap 7.92 ( https://nmap.org ) at 2022-02-09 14:16 EST', 'Nmap scan report for 10.159.238.5', 'Host is up (0.047s latency).', 'Nmap scan report for 10.159.238.10', 'Host is up (0.10s latency).', 'Nmap scan report for 10.159.238.14', 'Host is up (0.10s latency).', 'Nmap scan report for annies-mbp.new-albany.k12.oh.us (10.159.238.15)', 'Host is up (0.047s latency).', 'Nmap scan report for meekos-mbp.new-albany.k12.oh.us (10.159.238.18)', 'Host is up (0.097s latency).', 'Nmap scan report for 10.159.238.20', 'Host is up (0.17s latency).', 'Nmap scan report for 10.159.238.21', 'Host is up (0.10s latency).', 'Nmap scan report for madisons-galaxy-s9.new-albany.k12.oh.us (10.159.238.22)', 'Host is up (0.13s latency).', 'Nmap scan report for 10.159.238.24', 'Host is up (0.13s latency).', 'Nmap scan report for na-howard.13-26067 (10.159.238.27)', 'Host is up (0.099s latency).', 'Nmap scan report for 10.159.238.31', 'Host is up (0.10s latency).', 'Nmap scan report for 10.159.238.39', 'Host is up (0.072s latency).', 'Nmap scan report for na-stewart.12-23589 (10.159.238.43)', 'Host is up (0.045s latency).', 'Nmap scan report for mahdis-mbp.new-albany.k12.oh.us (10.159.238.46)', 'Host is up (0.047s latency).', 'Nmap scan report for elliots-mbp.new-albany.k12.oh.us (10.159.238.69)', 'Host is up (0.046s latency).', 'Nmap scan report for 10.159.238.87', 'Host is up (0.043s latency).', 'Nmap done: 256 IP addresses (16 hosts up) scanned in 1.61 seconds']
b = []
p = [x for x in a if "Nmap scan report for " in x]
for item in p:
    c = item.replace("Nmap scan report for ", "")
    b.append(c)

#u = [x for x in b if "(" and "ann" in x]
for x in b:
    if "(" and search1 in x:
        print(x + "\n")
    if "(" and search2 in x:
        print(x + "\n")
    if "(" and search3 in x:
        print(x + "\n")
    if "(" and search4 in x:
        print(x + "\n")
if b == "[]":
    print(Fore.RED + Back.BLACK +'Nothing Found :( \n' + Style.RESET_ALL)
