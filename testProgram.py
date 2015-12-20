import Initializer, HardwareInterfaces, Stimuli, DebugLogger, DataSavingFunctions, RandomizingFunctions, GlobalVariables
from psychopy import visual, core, event

Initializer.setup()
GlobalVariables.mouseClick = HardwareInterfaces.Mouse()

#testStimulus = Stimuli.GenericStimulus(0, 0, 10, "Green", "White", "Rect", "test_stimulus", 0, 200, 400)
#testStimulus.draw()

#Stimuli.updateScreen()
#core.wait(5)

testStimulus2 = Stimuli.GenericStimulus(0, 500, 10, "Green", "White", "Circle", "test_stimulus", 0, 200)
testStimulus3 = Stimuli.GenericStimulus(0, -500, 10, "Red", "White", "Circle", "test_stimulus", 0, 200)

testStimulus2.draw()
testStimulus3.draw()
Stimuli.updateScreen()

targetClicked, targetFlag, clickNum, reactionTimes = Stimuli.waitForClicks(2, [testStimulus2, testStimulus3], 20)

print ("target clicked: " + str(targetClicked) + " target flag: " + str(targetFlag) + " click num: " + str(clickNum) + " reactionTimes: " + str(reactionTimes))

dataSheet = DataSavingFunctions.Spreadsheet("test_data", ".")

dataSheet.addRowDataToList("First Column")
dataSheet.addRowDataToList("Second Column")
dataSheet.writeRow()
dataSheet.addRowDataToList("Second Row, 1st column")
dataSheet.addRowDataToList("Second Row, 2nd column")
dataSheet.writeRow()



randomizer = RandomizingFunctions.RiggedRandomizer(12, .5) # Todo: make math work here
print(randomizer.getList())

#GlobalVariables.mouseClick.waitForExitPress()