from player import Player
from ingredient import Ingredient
from room import Room
from weapon import Weapon
######### LOCAL IMPORTS ###################

import time



george_room = Room("george_room", "George's Room", "intro room", ["front_room", "upstairs_room"], None, None, "normal", None)

front_room = Room("front_room", "Front Room", "front room", ["kitchen", "upstairs_room"], None, None, "normal", None)

upstairs_room = Room("upstairs_room", "Upstairs", "upstairs", ["curts_room", "front_room"], None, None, "normal", None)

curts_room = Room("curts_room", "Curt's Room", "curts room", ["upstairs_room"], None, None, "normal", None)

kitchen_room = Room("kitchen_room", "Kitchen", "kitchen", ["front_room"], None, None, "normal", None)

player = Player("George", "this is george", 100, 0, [], [], {}, george_room)

room_list = [george_room, front_room, upstairs_room, curts_room, kitchen_room] 


xedi_list = ["x", "e", "d", "i", "p", "e", "x"]

def xedipex(mylist): 
	for i in range(len(mylist)+1): 
		print(" ".join(mylist[:i]))
		time.sleep(0.1)
	for i in range(1, len(mylist)+1): 
		print(" ".join(mylist[:-i]))
		time.sleep(0.1)


def title_screen(xedi_list): 
	print("\nWelcome to 'George Makes a Sandwich' a XEDIPEX GAME: ")
	time.sleep(3)
	xedipex(xedi_list)


def normal_room(room):
	
	print(f"\nYour in: {room.name}\n")
	print(f"{room.description}\n")
	print(f"You can move to these rooms: \n")

	for item in room.adj_room: 
		print(f"\t{item}\n")
	
	while True:
		user_input = input(">>> ")
		

def main():
	title_screen(xedi_list)

	while True:
		normal_room(player.current_room)


if __name__ == "__main__":
	main()