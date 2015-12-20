from psychopy import visual
from psychopy import parallel, event, core
from sys import platform as _platform
import sys
import GlobalVariables, DebugLogger, HardwareInterfaces
import multiprocessing

'''
Initializes back-end, like OS and PsychoPy variables

@author: Bradley Poulette
'''

def setup():
  #Determine which OS is being used, and calculate the screen size
  if _platform == "linux" or _platform == "linux2":
      # Linux
      import Tkinter
      
      root = Tkinter.Tk()

      GlobalVariables.screen_width = root.winfo_screenwidth()
      GlobalVariables.screen_height = root.winfo_screenheight()
      
      print("_width: " + str(GlobalVariables.screen_width) + "\n" + "height: " + str(GlobalVariables.screen_height))
      
  elif _platform == "win32":
      # Windows...
     from win32api import GetSystemMetrics
     print "width =", GetSystemMetrics (0)
     print "height =",GetSystemMetrics (1) 
     GlobalVariables.screen_width = GetSystemMetrics (0)
     GlobalVariables.screen_height = GetSystemMetrics (1)

  #Intializes and prints first line in logger
  GlobalVariables.logger = DebugLogger.DebugLogger("./")
  GlobalVariables.logger.writeToLog("Logger intialized")

  #Check to see if an operant box is connected
  GlobalVariables.apparatusPresent = HardwareInterfaces.checkForApparatus()

  #initialize the PsychoPy variables
  GlobalVariables.win = visual.Window(fullscr = True, rgb = [-1.000,-1.000,-1.000], units = "pix", winType = "pyglet")
  GlobalVariables.mouse = event.Mouse(visible = True)
  core.checkPygletDuringWait = True
  GlobalVariables.parallelPort = parallel.ParallelPort(address=0x0378)
