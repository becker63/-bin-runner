import multiprocessing.dummy
import multiprocessing
import socket
import re
import subprocess

out = []

def naocheck(ip):
    runfile = "sudo bash -c 'cd /home/becker/nao-fun/pynaoqi && python2 /home/becker/nao-fun/ansible/multiproc/scan/check.py" +' '  + str(ip) + "' "
    p = subprocess.Popen([runfile], stdout=subprocess.PIPE, shell=True)
    a = p.stdout.read()

    for line in a:
        if ip in line:
            print(line)

def namecheck(ip):
   a = socket.getfqdn(ip)
   print(a)
   #b = re.sub('[\d\.]', '', a)
   c = None
   if ('nao' in a) or ('eva' in a) or ('bas' in a):
       c = a
   else:
       c = ''
   if not c == '':
     out.append(f'{ip}')

def ping_range(start, end, num_threads, host):
    num_threads = 2 * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)
    p.map(namecheck, [host + str(x) for x in range(start,end)])


n = 200
sub = "10.159"
for i in range(225, 255):
    ping_range(0, 255, 100, f'{sub}.{i}.')

print("\n\n\n\n\n\n" + str(out))   
for line in out:
    naocheck(line)