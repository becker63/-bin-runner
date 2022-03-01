from datetime import datetime
start_time = datetime.now()
import sys
sys.path.append('/home/becker/nao-fun/pynaoqi')
from naoqi import ALProxy


import time
#time.sleep(2)

data=[]
ip2 = str(sys.argv[1])
ip = ip2[-2:]
##print(str(ip2))

end_time = datetime.now()

fulltime = end_time - start_time
#print('time:' + str(fulltime)[-9:])


time2 = str(sys.argv[2])

count = "" + str(sys.argv[3])

time3 = float(time2) * int(count)
##print(count)

#print("\ncalc: " + str(time3))

time.sleep(time3)




#from naoqi import AL#Proxy
#tts = AL#Proxy("ALTextToSpeech", ip2, 9559)
#tts.say("hello")
