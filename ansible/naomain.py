#note: because alderbran sucks this is 2.7
import sys
sys.path.append('/home/becker/nao/naoqi/pynaoqi')
from naoqi import ALProxy
ip = str(sys.argv[1])
tts = ALProxy("ALTextToSpeech", ip, 9559)
tts.say("w")
