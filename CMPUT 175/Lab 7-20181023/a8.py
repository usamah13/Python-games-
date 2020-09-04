from maze import Maze
from maze import MazeSquare
from Stack import Stack

def test_maze(maze):
	stack = Stack()
	stack.push(maze.get_start_square())

	while not stack.is_empty():
		current_square = stack.pop()
		if maze.is_finish_square(current_square):
			return True
		for square in current_square.get_legal_moves():
			stack.push(square)
	return False

def main():
	filename = input("Enter File Name for Maze: ")
	maze = Maze(filename)
	if test_maze(maze) == True:
		print("Goal is reached")
	elif test_maze(maze) == False:
		print("Goal is Unreachable")
	else:
		print("Goal is Unreachable")

main()