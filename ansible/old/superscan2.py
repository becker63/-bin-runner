import multiprocessing.dummy
import multiprocessing
import socket
import re


out = []

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
     out.append(f'{ip} : {c}')

def ping_range(start, end, num_threads, host):
    num_threads = 2 * multiprocessing.cpu_count()
    p = multiprocessing.dummy.Pool(num_threads)
    p.map(namecheck, [host + str(x) for x in range(start,end)])


n = 200
sub = input("enter sub: ")
for i in range(225, 255):
    ping_range(0, 255, 100, f'{sub}.{i}.')

print("\n\n\n\n\n\n" + str(out))   
for line in out:
    print(line)