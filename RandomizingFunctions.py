'''
	A class that creates a list of a specified size, and fills it
	with a specified proportion on 1's and 0's for pseudo-randomization.

	@author: Bradley Poulette
'''

class RiggedRandomizer:

	def __init__(self, listSize, percentCorrect):

		self.listSize = listSize;
		self.percentCorrect = percentCorrect;
		self.values = [];
		self.index = 0;
		rolledBefore = False;

		self.populateList(self.listSize, self.percentCorrect);

	def populateList(self, listSize, percentCorrect):

		# To avoid erroneous calls with non-decimal percentage values
		if percentCorrect >= 1:
			percentCorrect = 1

		numberCorrect = percentCorrect*listSize;

		'''if numberCorrect > 0:			# TODO: Make so that number rounds up if value is decimal
			numberCorrect += 1'''

		for i in range (0, int(numberCorrect)):
			self.values.append(1);
		for i in range (int(numberCorrect), listSize):
			self.values.append(0);

	def getCurrentVal(self):

		val = self.values[self.index];
		self.index += 1;
		return val;

	def reset(self):

		self.index = 0;
		rolledBefore = False;
		populateList(listSize, percentCorrect);

	def getList(self):
		return self.values
