#!/usr/bin/env python

size_map = [3, 4]
position = [0, 0]

def start():
	while True:
		action = input("You're at (" + str(position[0]) + ", " + str(position[1]) + "), what would you like to do? (north, south, east, west\n>>> ")
		if action == "north":
			if position[0]-1 >= 0:
				position[0] = position[0]-1
			else:
				print("/!\\ You cannot go outside the map /!\\")
		elif action == "south":
			if position[0]+1 < size_map[0]:
				position[0] = position[0]+1 
			else:
				print("/!\\ You cannot go outside the map /!\\")
		elif action == "east":
			if position[1]+1 < size_map[1]:
				position[1] = position[1]+1
			else:
                        	print("/!\\ You cannot go outside the map /!\\")
		elif action == "west":
			if position[1]-1 >= 0:
				position[1] = position[1]-1
			else:
                        	print("/!\\ You cannot go outside the map /!\\")
		elif action == "exit":
			exit()
		else:
			print("/!\\ Direction " + action + " is not allowed /!\\")
		#print(position)

if __name__ == '__main__':
	start()
