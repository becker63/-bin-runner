import os
a_file = open(r"""C:\Users\becker\Documents\naobin.txt""", "r")

a = ""
for line in a_file:
  stripped_line = line.replace("\n", ":")
  a += stripped_line
a_file.close()

b = a.split(':')

for x in b:
    #os.system("sudo -u#-1" + x)
    print("sudo -u#-1 " + x)
