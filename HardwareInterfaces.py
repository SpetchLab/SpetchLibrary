from psychopy import parallel, core, event
import os, sys, inspect
import GlobalVariables
try{
	import readPort
} except {
	try{
		 # use this if you want to include modules from a subfolder
		 cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
		 if cmd_subfolder not in sys.path:
		     sys.path.insert(0, cmd_subfolder)
	}
}

'''
	Connects to a port and allows binary manipulation

	Example: raise/lower an operant box hopper

	portValue: a hexadecimal number use to represent the current values on the port
	parallelPort: a pre-created ParallelPort with an existing address
	maskValue: a hexadecimal number representing a bitmask which flips bits on the port
	
	@author: Bradley Poulette
'''
class HardwareInterface:

	def __init__(self, portValue, parallelPort, mask = 0x0000):
		self.portValue = portValue;
		self.parallelPort = parallelPort;
		self.maskValue = mask

	def turn_on(self):
		portValue = portValue | (maskValue);
		parallelPort.setData(portValue);
		return portValue;

	def turn_off(self):
		portValue = portValue & ~(maskValue);
		parallelPort.setData(portValue);
		return portValue;


class Mouse:

	def waitForExitPress(self, time = 0):
	  GlobalVariables.logger.writeToLog("Waiting for user to press escape")
	  if time == 0:
	    while True:
	      if event.getKeys(["escape"]):
	            GlobalVariables.logger.writeToLog("User pressed escape")
	            exit()
	  else:
	    waitTimer = core.CountdownTimer(time) 
	    while (waitTimer.getTime() > 0):
	      if event.getKeys(["escape"]):
	            GlobalVariables.logger.writeToLog("User pressed escape")
	            exit()

def readValue(self, portValue, mask):
	return (readPort.readPort(portValue) & mask)

#Reads IR beam status on port 0x0201 (GamePort)
def checkForApparatus():
  #return True if apparatus present, False otherwise

  try{
	  value = readPort.readPort(0x0201)
	  GlobalVariables.logger.writeToLog("Apparatus value " + str(value))
	  if value == 0x00ff:
	    return True
	  else:
	    return False
  } except {
  	  return false
  }