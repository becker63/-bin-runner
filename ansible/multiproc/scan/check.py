import sys
sys.path.append('/home/becker/nao-fun/pynaoqi')

ip2 = str(sys.argv[1])

from naoqi import ALProxy


try:
    tts = ALProxy("", ip2, 9559)
    tts.say("")
except RuntimeError as e:
    print("invaid host " + ip2)


