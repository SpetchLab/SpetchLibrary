'''
A program which interfaces with PYBox systems for behavioural experiments
'''

import sys
import glob
import serial


class keyLight:
	def __init__(self, name, startColour, position):
		  self.colour = startColour
          self.name = name
          self.timeout = 10
          self.position = position

    def setColour(self, colour):
    	self.colour = colour

   	def setTimeout(self, value):
   		self.timeout = value

   	def on(self):
   		#Send value to serial
   		#if self.positon == ...

   	def off(self):
   		#send value to serial
   		#if self.positon == ...


def scanUSBPorts():
	"""Lists serial ports

	Retrieved from: http://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
	on June 1, 2015

	:author:
		Thomas
    :raises EnvironmentError:
        On unsupported or unknown platforms
    :returns:
        A list of available serial ports
    """
    if sys.platform.startswith('win'):
        ports = ['COM' + str(i + 1) for i in range(256)]

    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this is to exclude your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')

    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')

    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def setup():
	global usbPort
	availablePorts = scanUSBPorts()
	for i in range(0, len(availablePorts)):
		#read serial information and check authentication

	key1 = keyLight("key_1", "red", position)
	key2 = keyLight("key_2", "green", position)
	key3 = keyLight("key_3", "blue", position)


def houseLightToggle():
	#send value to serial


def readHopperIR():


def hopperPositionToggle():


def hopperLightToggle():



def main():



#Called when the experiment starts.
if __name__ == "__main__":
    main()