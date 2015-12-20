import os, csv

'''
	Creates and writes to a .csv file

	@author: Bradley Poulette
'''

class Spreadsheet:

	def __init__(self, filename, path):
		self.path = path;
		self.filename = filename;

		self.rowDataList = [];

		filename = path + '/' + filename + '.csv'
		if not os.path.exists(path):
			os.makedirs(path)
		datafile = open(filename, 'wb')
		self.writer = csv.writer(datafile, delimiter=',')

	def addRowDataToList(self, rowDataString):
		self.rowDataList.append(rowDataString);

	def writeRow(self):
		self.writer.writerow(self.rowDataList);
		self.rowDataList = []

	def newRow(self):
		self.rowDataList = []

