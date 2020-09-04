import sys
import re
import operator

def readFile(filepath):
	try:
		with open(filepath) as f:
			lines = f.read().splitlines()
			return lines
	except IOError:
		print ("File Not Found.")
		sys.exit()

def parseLine(line):
	data = {}
	wordPair = line.split(" ")
	data['city'] = wordPair[0]
	data['amt'] = float(wordPair[1])
	#print(data)
	return data

def formatFloat(input):
	#stringRevised = "{0:>5.2f}".format(input)
	stringFloat = "%.2f" % input
	stringLength = len(stringFloat)
	spacesToAdd = 5 - stringLength
	stringRevisedLength = len(stringFloat) + spacesToAdd
	stringRevised = stringFloat.rjust(stringRevisedLength)	
	return stringRevised

def formatString(input):
	#stringRevised = "{0:^25}".format(input)
	stringLength = len(input)
	spacesToAdd = 25 - stringLength
	stringRevisedLength = stringLength + spacesToAdd
	stringRevised = input.center(stringRevisedLength)	
	return stringRevised.upper()

def writeToFile(input, mode, filePath):
	#LINES_WRITTEN = 0
	file = open(filePath, mode)
	line = input
	file.write(line)
	#if(file.write(line)):
		#LINES_WRITTEN = LINES_WRITTEN + 1
	#else:
		#return -1
	file.close()
	#return LINES_WRITTEN

def writeResultToFile(inputHeading, inputRange, filepath):
	writeToFile(inputHeading + "\n", "a", filepath)
	for data in inputRange:
		stringCityRevised = formatString(data['city'])
		stringRainRevised = formatFloat(data['amt'])
		writeToFile(stringCityRevised +" "+ stringRainRevised + "\n", "a", filepath)
def main():
	
	rangeOne = []	#[0-51)
	rangeTwo = []	#[51-61)
	rangeThree = []	#[61-71)
	rangeFour = []	#[71-81)
	rangeFive = []	#[81-91)
	rangeSix = []	#[91-101)
	
	rainFallFilePath = "rainfall.txt"
	resultFilePath = "result.txt"
	
	cityData = []
	fileLines = readFile(rainFallFilePath)
	
	for line in fileLines:
		dataLine = parseLine(line)
		cityData.append(dataLine)
	
	for data in cityData:
		if data['amt'] >= 0.0 and data['amt'] < 51.0:
			rangeOne.append(data)
		elif data['amt'] >= 51.0 and data['amt'] < 61.0:
			rangeTwo.append(data)
		elif data['amt'] >= 61.0 and data['amt'] < 71.0:
			rangeThree.append(data)
		elif data['amt'] >= 71.0 and data['amt'] < 81.0:
			rangeFour.append(data)
		elif data['amt'] >= 81.0 and data['amt'] < 91.0:
			rangeFive.append(data)
		elif data['amt'] >= 91.0 and data['amt'] < 101.0:
			rangeSix.append(data)
		else:
			print("Error rainfall amount out of range")
	
	rangeOne.sort(key=operator.itemgetter('amt'))
	rangeTwo.sort(key=operator.itemgetter('amt'))
	rangeThree.sort(key=operator.itemgetter('amt'))
	rangeFour.sort(key=operator.itemgetter('amt'))
	rangeFive.sort(key=operator.itemgetter('amt'))
	rangeSix.sort(key=operator.itemgetter('amt'))
	writeToFile("", "w", resultFilePath) # clear out contents of file
	
	writeResultToFile("[0-51)", rangeOne, resultFilePath)
	writeResultToFile("[51-61)", rangeTwo, resultFilePath)
	writeResultToFile("[61-71)", rangeThree, resultFilePath)
	writeResultToFile("[71-81)", rangeFour, resultFilePath)
	writeResultToFile("[81-91)", rangeFive, resultFilePath)
	writeResultToFile("[91-101)", rangeSix, resultFilePath)

main()