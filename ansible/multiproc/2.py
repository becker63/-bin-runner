from datetime import datetime
start_time = datetime.now()
import sys
sys.path.append('/home/becker/nao-fun/pynaoqi')

ip2 = str(sys.argv[1])

from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", ip2, 9559)
tts.say("DANIEL STOP WATCHING VIDEOS AND GET TO WORK!!!!")
