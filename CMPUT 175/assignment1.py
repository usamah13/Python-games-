#Assignment1
# A program that reads a text file with specfic animal ids and which stations it visited(only 2 possible stations)
# The program then outputs the number of times the each aninal has visited the station, animals that have visited
# both stations at least 4 times, toal number of visits for botth stations and the month with the highest number of vists

import sys #Module imported to deal with an error encountered in opening the file
import re  #Module imported to remove, find and subisitute specific charchters


def readFile(filepath): 
	# Funtion the that reads the file needed and returns a list of lines in that file
	# Found this technique online, where manula closure of thw file is no longer required
	# _filepath is the name of the file(user input) to be opened
	
	try: 
		with open(filepath) as f:
			lines = f.read().splitlines()
		return lines
	except IOError:
		print ("File Not Found.")
		sys.exit()
		
def cleanFileInput(lines):
	# Function that removes the empty lines and # comment lines from the list of lines, and rerurns the new cleanInput list
	#_lines the list of lines retrived from readfile function 
	
	cleanInput = []
	for line in lines:
		matchObj = re.match( r'^(\#).*', line, re.I)  #If a lines starts with a hash or emplty line, #True or False
		if (not (line == "" or matchObj)):  # If line is not hash or empty line append in to clean list 
			cleanInput.append(line)
	return cleanInput

def getAnimalList(lines):
	# This fucntion generates a list of animals called anaimals from the new cleanInput list, and replaces the id character to a 
	#_lines is the list of lines returned from the cleanInput function
	
	animals = []
	for line in lines:
		wordPair = line.split("#") # Splits the line in to 2 respective strings at #
		animalID = re.sub(r'^id', "a", wordPair[0]) #to find the 'id' charchters in the line and change to 'a'
		if animalID not in animals:
			animals.append(animalID)
	animals.sort()
	return animals

def getMonthList(lines):
	# This fucntion generates a list of months from the new cleanInput list, searches for the month in the string then adds it
	#_lines is the list of lines returned from the cleanInput function
	
	months = []
	for line in lines:
		wordPair = line.split("#") # Splits the line in to 2 respective strings at #
		regex_exp = re.compile('^\d+')
		s = regex_exp.search(wordPair[1]) # searching for the month, a regex technique I learned
		month = s.group() #extracts the first instance of the searh (means the first time intger month apperead in the string) 
		if month not in months:
			months.append(month)
	months.sort(reverse=True) # to make sure the last month alwasy gets printed for section4
	return months

def getStation1(lines):
	#This Funstion makes a dictionary station1 with the animals as keys and number of times the animal visited station 1 as values 
	#_lines is the list of lines returned from the cleanInput function
	
	station1 = {}
	for line in lines:
		wordPair = line.split("#")
		animalID = re.sub(r'^id', "a", wordPair[0]) 
		if (wordPair[2] == "s1"):
			if animalID in station1:
				station1[animalID] += 1
			else:
				station1[animalID] = 1
	return station1

def getStation2(lines):
	#This Funstion makes a dictionary station2 with the animals as keys and number of times the animal visted station 2 as values 
	#_lines is the list of lines returned from the cleanInput function
	
	station2 = {}
	for line in lines:
		wordPair = line.split("#")
		animalID = re.sub(r'^id', "a", wordPair[0]) 
		if (wordPair[2] == "s2"):
			if animalID in station2:
				station2[animalID] += 1
			else:
				station2[animalID] = 1
	return station2

def getMonthlyVisits(lines):
	#This Funstion makes a dictionary that records the number of visits that occurred for station1 and station2 for each month.
	#_lines is the list of lines returned from the cleanInput function
	
	monthlyVisits = {}
	for line in lines:
		wordPair = line.split("#")
		regex_exp = re.compile('^\d+')
		s = regex_exp.search(wordPair[1])
		month = s.group()
		if month in monthlyVisits:
			monthlyVisits[month] += 1
		else:
			monthlyVisits[month] = 1
	return monthlyVisits

def print_section1(animal_list, station1, station2):
	# This function prints outputs a table with the animal ids  and the number of time that aniaml visted station 1 and station 2
	#_animal_list is the list of animals
	#_station1 is a dictionary that records frequency of visit of each animal to station 1
	#_station2 is a dictionary that records frequency of visit of each animal to station 2 

	print("Number of times each animal visited each station")
	heading = "{0:^20}{1:^20}{2:^20}".format("Animal Id", "Station 1", "Station 2")
	heading =  heading + "\n" + (60*"=")
	print(heading)
	for element in animal_list:
		station_1_Value = 0
		station_2_Value = 0
		if element not in station1:
			station_1_Value = 0
		else:
			station_1_Value = station1[element]
		if element not in station2:
			station_2_Value = 0
		else:
			station_2_Value = station2[element]
		table = "{0:^20}{1:^20}{2:^20}".format(element, station_1_Value, station_2_Value)
		print(table)

def print_section2(animal_list, station1, station2):
	#The aminals that visted both stations at least 4 times are found
	#_animal_list is the list of animals
	#_station1 is a dictionary that records frequency of visit of each animal to station 1
	#_station2 is a dictionary that records frequency of visit of each animal to station 2 
	
	print("Animals that visted both stations at least 4 times")
	for element in animal_list:
		if element in station1 and element in station2 and station1[element] >= 4 and station2[element] >= 4:
			print(element)

def print_section3(animal_list, station1, station2):
	# The total number of vists that each animal has to both stations is caluclated and printed out
	#_animal_list is the list of animals 
	#_station1 is a dictionary that records frequency of visit of each animal to station 1
	#_station2 is a dictionary that records frequency of visit of each animal to station 2 	
	print("Total Number of visits for each animal")
	for element in animal_list:
		station_1_Value = 0
		station_2_Value = 0
		if element not in station1:
			station_1_Value = 0
		else:
			station_1_Value = station1[element]
		if element not in station2:
			station_2_Value = 0
		else:
			station_2_Value = station2[element]
		totalVisits = station_1_Value + station_2_Value
		visits_string = element + " " + str(totalVisits)
		print(visits_string)

def print_section4(monthly_list, monthly_visits):
	# Prints out the last month which had the highest number of visits
	#_monthly_list is a list of all months that exists
	#_monlthy_visits is a dictionary that records the number of visits that occurred for station1 and station2 for each month
	
	print("The month with the highest number of visits to the stations")
	highest_month  = ""
	highest_value =  0
	for month in monthly_list:
		if month in monthly_visits and monthly_visits[month] > highest_value:
			highest_month = month
			highest_value = monthly_visits[month]
	month_string = "Month " + highest_month + " has " + str(highest_value) + " visits"
	print(month_string)


def main():
	
	#Opening, reading and cleaning the flie
	
	fileName = input('Enter filename >')
	reading_file = readFile(fileName)
	lines = cleanFileInput(reading_file)

	#creating the required data sturctres
	
	animal_list = getAnimalList(lines)
	month_list = getMonthList(lines)
	station1 = getStation1(lines)
	station2 = getStation2(lines)
	monthly_visits = getMonthlyVisits(lines)
	dashes_string = (60*"-")
	#Printing each spectic section as required
	print_section1(animal_list, station1, station2)
	print(dashes_string)
	print_section2(animal_list, station1, station2)
	print(dashes_string)
	print_section3(animal_list, station1, station2)
	print(dashes_string)
	print_section4(month_list, monthly_visits)




main()