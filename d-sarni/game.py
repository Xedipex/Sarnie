from player import Player
from ingredient import Ingredient
from room import Room
from weapon import Weapon
######### LOCAL IMPORTS ###################

import time


player = Player("George", "this is george", 100, 0, [], [], {})

intro = Room("George's Room", "intro room", ["Front Room", "Upstairs"], None, None, "intro", None)

mylist = ["x", "e", "d", "i", "p", "e", "x"]

def xedipex(mylist): 
	for i in range(len(mylist)+1): 
		print(" ".join(mylist[:i]))
		time.sleep(0.1)
	for i in range(1, len(mylist)+1): 
		print(" ".join(mylist[:-i]))
		time.sleep(0.1)

def intro_room(room, mylist):
	print("\nWelcome to 'George Makes a Sandwich' a XEDIPEX GAME: ")
	time.sleep(3)
	xedipex(mylist)
	print(f"\nYour in: {room.name}\n")
	print(f"{room.description}\n")
	print(f"You can move to these rooms: \n")
	for item in room.adj_room: 
		print(f"\t{item}\n")


def main():
	intro_room(intro, mylist)

if __name__ == "__main__":
	main()