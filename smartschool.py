import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import json
from gtts import gTTS
import os

#Provide your IBM Watson Device Credentials
organization = "iwl46m"
deviceType = "iotsensors"
deviceId = "1002"
authMethod = "token"
authToken = "9?s+!f4O3bo8Ii&sV*"

 



# Initialize the device client.
notice=" "
def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data['command'])
        notice=cmd.data['command']
        language='en'
        output=gTTS(text=notice,lang=language,slow=False)

        output.save("output.mp3")

        os.system("start output.mp3")
        






try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        time.sleep(1)
        deviceCli.commandCallback = myCommandCallback
        time.sleep(5)
        p=random.randint(0,1)

        if p==1:
           print("switch on")
        else:
           print("switchoff") 
        

        

# Disconnect the device and application from the cloud
deviceCli.disconnect()
