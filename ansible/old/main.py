from termcolor import colored
import multiprocessing.dummy
import multiprocessing
import os
import subprocess
import time as sleeper
import re
import timeit
from timeout import timeout
exectime = 0.0
exectime2 = 0.0
total = []

def runner(ip, runfile):
      try:
        #print(runfile2)
        global exectime
        a = subprocess.check_output(runfile2, shell=True).decode('ascii')
        print(a)
        f = a.splitlines()
        for item in f:
              print(item)
              if 'time:' in item:
                    b = item.split(':')
                    for item in b:
                          if '.' in item:
                                exectime = float(item)
                                return(exectime)
              if 'calc:' in item:
                    c = item.split(':')
                    for item in c:
                          if '.' in item:
                                exectime2 = float(item)
                                return(exectime2)
                            #print("\n" + str(exectime) + "\n\n")    
                                             
      #print("\n\n" + ip)
      except subprocess.CalledProcessError as e:
        print(e.output)

os.system('clear')
def ping(ip, time, runfile2):
    #print("====================================================")
    #print("")
    #sleeper.sleep(2)
    runner(ip, runfile2)
    #print("")
    #print("====================================================")
    #print("")


def runner2():
            print(i)
            #print(colored(exectime2, 'green'))
            
            #print(colored(runfile2, 'red')) 
            ping(item, 1, runfile2)



i = 0
if __name__ == "__main__":
    with open('hosts', 'r') as file:
      data = file.read()
      data2 = str(data).replace('[sites]', '')
      #print(data2)
      data3 = data2.splitlines()
      del data3[0]
      #print(data3)



