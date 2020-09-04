from Stack import Stack
import sys
import re

def main():
	HOMEPAGE = "www.cs.ualberta.ca"
	forward_stack = Stack()
	back_stack = Stack()
	elementInserted = 0
	backPressed = 0
	back_stack.push(HOMEPAGE)
	print("Welcome to web browser navigation")
	print("Current url: [" + back_stack.peek() + "]")
	cmd = input("Enter command: > for forward, < for backward, = for a new url, or x for exit: ")
	while cmd != "x":
		if cmd == "<":
			backPressed = 1
			if elementInserted == 0:
				print("< is an invalid action")
				print("Current url: [" + back_stack.peek() + "]")
			elif back_stack.size() == 1:
				print("< is an invalid action")
				print("Current url: [" + back_stack.peek() + "]")
			else:
				forward_stack.push(back_stack.pop())
				print("Current url: [" + back_stack.peek() + "]")
		elif cmd == ">":
			backPressed = 0
			if elementInserted == 0:
				print("> is an invalid action")
				print("Current url: [" + back_stack.peek() + "]")
			elif forward_stack.is_empty():
				print("> is an invalid action")
				print("Current url: [" + back_stack.peek() + "]")
			else:
				back_stack.push(forward_stack.pop())
				print("Current url: [" + back_stack.peek() + "]")
		elif cmd == "=":
			elementInserted = elementInserted + 1
			urlToPush = input("Enter a new url: ")
			back_stack.push(urlToPush)
			print("Current url: [" + back_stack.peek() + "]")
			if backPressed == 1:
				forward_stack = Stack()
				backPressed = 0
		else:
			print(cmd + " is an invalid action")

		cmd = input("Enter command: > for forward, < for backward, = for a new url, or x for exit: ")

main()