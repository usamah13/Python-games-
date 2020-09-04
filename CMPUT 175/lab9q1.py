from CircularQueue import CircularQueue

def printQueues(list_1, list_2):
	normalQueueString = str(list_1)
	vipQueueString = str(list_2)
	statement = "Normal customers queue: " + normalQueueString + " \n" + "VIP customers queue: " + vipQueueString +"\n"
	print(statement)


def main():
	normalQueue = CircularQueue(3)
	vipQueue = CircularQueue(3)

	command = input("Add, Serve, or Exit: ")
	while (command != "Exit"):
		if command == "Add":
			name = input("Enter the name of the person to add: ")
			isVIP = input("Is the customer VIP? ")
			if isVIP == "True":
				if vipQueue.isFull():
					print("Error: VIP customers queue is full")
				else:
					vipQueue.enqueue(name)
					statement = "add " + name + " to VIP line"
					print(statement)
			elif isVIP == "False":
				if normalQueue.isFull():
					print("Error: Normal customers queue is full")
				else:
					normalQueue.enqueue(name)
					statement = "add " + name + " to the line"
					print(statement)
			else:
				print("Wrong Command. Please Enter True or False")
				#break
				#isVIP = input("Is the customer VIP? ") #?
				
		elif command == "Serve":
			if vipQueue.isEmpty() and normalQueue.isEmpty():
				print("Error: Queues are empty")
			else:
				if not vipQueue.isEmpty():
					served = vipQueue.dequeue()
					statement =  served + " has been served"
					print(statement)
				else:
					served = normalQueue.dequeue()
					statement =  served + " has been served"
					print(statement)
		else:
			print("Wrong Command. Please Enter Add, Serve or Exit")
		printQueues(normalQueue, vipQueue)
		command = input("Add, Serve, or Exit: ")
	print('Quiting')

main()