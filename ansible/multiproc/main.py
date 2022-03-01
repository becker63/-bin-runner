from termcolor import colored
import subprocess
import os
import time

files = []

with open('hosts', 'r') as file:
    data1 = file.read()
    files2 = data1.split("\n")

    for item in files2:
        appe = item + "'"
        print(appe)
        files.append(appe)
        
cmd = "sudo bash -c 'cd /home/becker/code/nao-fun/pynaoqi && python2 /home/becker/code/nao-fun/ansible/multiproc/3.py"
processes = set()
max_processes = 5

for name in files:
    command = f"{cmd} {name}"
    print(colored(command, 'green'))
    processes.add(subprocess.Popen(command, shell=True))
    if len(processes) >= max_processes:
        os.wait()
        processes.difference_update(
            [p for p in processes if p.poll() is not None])
#Check if all the child processes were closed
for p in processes:
    if p.poll() is None:
        p.wait()