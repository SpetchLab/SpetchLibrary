import GlobalVariables
from psychopy import visual, core, parallel, gui, event

'''
	A simplified class for accessing PsychoPy stimuli

	@author: Bradley Poulette
'''

# Draws rectangles and circles with an outline. 
# If more shapes are needed, use Psychopy.visual objects, as defined at:
# http://www.psychopy.org/api/visual.html
class GenericStimulus:

	def __init__(self, x, y, lineWidth, fillColour, outlineColour, shape, name, timeout, height, width = 0, assocStims = []):

		self.x = x;
		self.y = y;
		self.height = height;
		if width == 0:	
			self.width = self.height;
		else:
			self.width = width
		self.lineWidth = lineWidth
		self.fillColour = fillColour;
		self.outlineColour = outlineColour;
		self.shape = shape;
		self.name = name;
		self.timeout = timeout;
		self.assocStims = assocStims;
		self.boundingBox = 0
		self.coreStim = 0

	def addAssocStim(self, genericStim):
		self.assocStims.append(genericStim);

	# Draws stimuli, but does NOT update the display to show them
	# MUST call Stimuli.updateScreen() to display drawn stimuli
	def draw(self):

		if self.shape == "Circle":
			self.boundingBox = visual.Circle(GlobalVariables.win, lineWidth = self.lineWidth, radius = self.width, pos = (self.x, self.y), units = "pix", lineColor = self.outlineColour, fillColor = "White")
			self.coreStim = visual.Circle(GlobalVariables.win, lineWidth = self.lineWidth, radius = self.width, pos = (self.x, self.y), units = "pix", lineColor = self.outlineColour, fillColor = self.fillColour)
		elif self.shape == "Rect":
			self.boundingBox = visual.Rect(GlobalVariables.win, lineWidth = self.lineWidth, width = self.width, height = self.height, pos = (self.x, self.y), units = "pix", lineColor = self.outlineColour, fillColor = "White")
			self.coreStim = visual.Rect(GlobalVariables.win, lineWidth = self.lineWidth, width = self.width, height = self.height, pos = (self.x, self.y), units = "pix", lineColor = self.outlineColour, fillColor = self.fillColour)

		self.boundingBox.draw()
		self.coreStim.draw()

	def drawAssocStims(self):
		for stim in self.assocStims:
			stim.draw()

	def removeStim(self, stimulus):
		self.assocStims.remove(stimulus)

	def getBoundingBox(self):
		return self.boundingBox

class TextStimulus:

	def __init__(self, content, position, alignment = "Top"):
		self.content = content
		self.position = position
		self.alignment = alignment

		self.textStim = visual.TextStim(GlobalVariables.win, text=content, pos=position, alignVert = alignment)

	def draw(self):
		self.textStim.draw()

# Displays all stimuli drawn between the last update and this one
# MUST be called in order to see stimuli drawn
def updateScreen():
	GlobalVariables.win.flip()

# Waits for input on any object provided in "Stimuli"
# Returns after "targetPeckRequired" number of clicks on
# stimuli is reached.
# Returns target stimulus clicked, target click flag, 
# total number of clicks, and reaction times for each click
def waitForClicks(targetClickRequired, stimuli, duration):

    GlobalVariables.logger.writeToLog("Waiting for " + str(targetClickRequired) + " clicks on " + str(len(stimuli)) + " stimuli for " + str(duration) + " seconds.")
    clickNum = 0
    targetClickNum = 0
    targetClicked = ""
    oldMouseIsDown = True

    targetFlag = False
    reactionTimes = []
    reactionTimer = core.Clock()
    stimTimer = core.CountdownTimer(duration)
    
    while ((stimTimer.getTime() > 0) and (targetFlag == False)):

      mouseIsDown = GlobalVariables.mouse.getPressed()[0]
      GlobalVariables.mouse.clickReset()

      if mouseIsDown and not oldMouseIsDown:

          # Add click reaction times to list.
          reactionTimes.append(reactionTimer.getTime())
          pos = GlobalVariables.mouse.getPos()

          for i in range (0,len(stimuli)):
            if stimuli[i].getBoundingBox().contains(pos):
              targetClickNum += 1
              if targetClickNum >= targetClickRequired:
                targetFlag = True
                targetClicked = stimuli[i]
                break

          reactionTimer.reset()
          clickNum += 1
       
      oldMouseIsDown = mouseIsDown

      if event.getKeys(["escape"]):
        GlobalVariables.logger.writeToLog("User pressed escape while waiting for clicks")
        exit()


    return targetClicked, targetFlag, clickNum, reactionTimes

