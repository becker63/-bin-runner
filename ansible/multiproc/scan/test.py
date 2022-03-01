import subprocess
import os


def naocheck(ip):
    runfile = "sudo bash -c 'cd /home/becker/nao-fun/pynaoqi && python2 /home/becker/nao-fun/ansible/multiproc/scan/check.py" +' '  + str(ip) + "' "
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()
    

    a = system_call(runfile).decode('ascii').split("\n")

    for line in a:
        if ip in line:
            print(line)