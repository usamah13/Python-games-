

import sys
import re

def readFile(filepath):
    try:
        with open(filepath) as f:
            lines = f.read().splitlines()
            return lines
    except IOError:
        print ("File Not Found.")
        sys.exit()

def parseQuake(line):

    data = {}
    wordPair = line.split("#")
    magnitude = wordPair[0]

    regex_exp = re.compile('\w+$')
    s = regex_exp.search(wordPair[1])
    region = s.group()

    regex_exp = re.compile('^(\d+/\d+/\d+)')
    s = regex_exp.search(wordPair[1])
    date = s.group()

    data['magnitude'] = magnitude
    data['region'] = region
    data['date'] = date

    return data

def main():
    earthQuakeDict = dict()

    earthQuakeFilePath = "earthquake.txt"

    fileLines = readFile(earthQuakeFilePath)

    for line in fileLines:
        data = parseQuake(line)
        #dateMagnitudeMappingString = "[" + data['date'] + ", " + data['magnitude'] + "]"
        templist = [data['date'],data['magnitude']]
        if data['region'] in earthQuakeDict:
            earthQuakeDict[data['region']].append(templist)
        else:
            earthQuakeDict[data['region']] = [templist]

    print("The Dictionary")
    print (earthQuakeDict)
    print(' ')
    print("Output after processing the dictionary")
    for key,value in earthQuakeDict:
        print (key + value)


main()