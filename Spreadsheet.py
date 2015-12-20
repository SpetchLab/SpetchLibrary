

class Spreadsheet:

	def __init__(self, filename, path):
		self.path = path;
		self.filename = filename;

		rowDataList = [];

		filename = path + '/' + filename + '.csv';
	    datafile = open(filename, 'wb');
	    writer = csv.writer(datafile, delimiter=',');

	def addRowDataToList(rowDataString):

		rowDataList.append(dataString);

	def writeRowDataListToRow():
		rowString = "";
		for i in range(0,len(rowDataList)):
			rowString = rowDataList[i] + ', ';

		writer.writeRow(rowString);

