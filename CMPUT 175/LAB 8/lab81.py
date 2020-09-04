import random as rnd
import os
import sys
import io
import re

def readAccounts(infile):
	result = {}
	line = infile.readline()
	while line:
		if line != '\n':
			wordPair = line.split(":")
			name = wordPair[0]
			amt = re.sub(r'\n', '', wordPair[1])
			#print(amt)
			if name not in result:
				try:
					float_amt =  float(amt)
					result[name] = float_amt
				except ValueError:
					print ("ValueError. Account for " + name + " not added: illegal value for balance")
		line = infile.readline()
	infile.close()
	return result

def processAccounts(accounts):
	while (True):
		try:
			accountName = input("Enter account name, or 'Stop' to exit: ")
			if accountName == "Stop":
				break
			else:
				#accounts[accountName]
				try:
					accountTransaction = input("Enter transaction amount for " + accountName + ": ")
					float_transaction =  float(accountTransaction)
					accounts[accountName] = accounts[accountName] + float_transaction
					print("New balance for account " + accountName + " : " +  str(accounts[accountName]))
				except ValueError:
					print ("Value Error.Incorrect Amount.Transaction canceled")
		except KeyError:
			print ("KeyError.Account does not Exist.Transaction cancelled.")

def main():
	try:
		filename = input ("Enter filename > ")
		file_object = open(filename, 'r')
		accounts = readAccounts(file_object)
		processAccounts(accounts)
	except IOError:
		print ("IOError.Input file does not exist")
		sys.exit()

main()