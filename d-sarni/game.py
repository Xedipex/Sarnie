from player import Player
from ingredient import Ingredient
from room import Room
from weapon import Weapon
######### LOCAL IMPORTS ###################

import re 
import time


################################################### INGREDIENTS ###############################################################

bread = Ingredient("bread", "Bread", "The foundation of life", 10, "bread")
cheese = Ingredient("cheese", "Cheese", "cheese", 9, "filling")
pickle = Ingredient("pickle", "Pickle", "Branston Original; of course", 100, "condiment")
mayo = Ingredient("mayo", "Mayo", "mayo", 999, "condiment")
lettuce = Ingredient("lettuce", "Lettuce", "lettuce", 5, "filling")
tomato = Ingredient("tomato", "Tomato", "tomato", 8, "filling")
onion = Ingredient("onion", "Onion", "onion", 7, "filling")
ham = Ingredient("ham", "Ham", "ham", 50, "meat")
chicken = Ingredient("chicken", "Chicken", "chicken", 60, "meat")
crown = Ingredient("crown", "Crown", "crown", 1, "crown")

################################################### INGREDIENTS ###############################################################


################################################### WEAPONS ###############################################################

gun = Weapon("gun", "Toy Gun", "toy gun", None, "weapon", 5, None, None)
stool = Weapon("stool", "Moss's Stool", "wooden stool", None, "weapon", 50, None, None)
football = Weapon("football", "Squishy Football", "football that squish", None, "weapon", 10, None, None)
water = Weapon("water", "Glass of Water", "water", None, ["weapon", "heal"], 10, 50, None)
zoot = Weapon("zoot", "Tim's Massive Zoot", "4/20 blaze it", None, "buff", None, None, 1.5)
vape = Weapon("vape", "Curt's Vape", "SMOK V9", None, "buff", None, None, 2.5)

################################################### WEAPONS ###############################################################


################################################### ROOMS ###############################################################

george_room = Room("george_room", "George's Room", "intro room", ["front_room", "upstairs"], [], [], "normal", None)

front_room = Room("front_room", "Front Room", "front room", ["kitchen", "upstairs"], [bread, lettuce], [], "normal", None)

upstairs_room = Room("upstairs", "Upstairs", "upstairs", ["curts_room", "front_room"], [], [water], "normal", None)

curts_room = Room("curts_room", "Curt's Room", "curts room", ["upstairs"], [], [], "normal", None)

kitchen_room = Room("kitchen", "Kitchen", "kitchen", ["front_room"], [], [], "normal", None)

player = Player("George", "this is george", 100, 0, [], [], {}, george_room)

################################################### ROOMS ###############################################################

room_list = [george_room, front_room, upstairs_room, curts_room, kitchen_room]

rooms = { 
	"george_room": george_room, 
	"front_room": front_room, 
	"upstairs": upstairs_room, 
	"curts_room": curts_room, 
	"kitchen": kitchen_room,
}

ingredients = { 
	"bread": bread, 
	"cheese": cheese, 
	"pickle": pickle, 
	"mayo": mayo, 
	"lettuce": lettuce, 
	"tomato": tomato, 
	"onion": onion, 
	"ham": ham, 
	"chicken": chicken, 
	"crown": crown
}

weapons = { 
	"gun": gun, 
	"stool": stool, 
	"football": football, 
	"water": water, 
	"zoot": zoot, 
	"vape": vape, 
}

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


def normal_room(room, player):
	
	print(f"\nYour in: {room.name}\n")
	print(f"{room.description}\n")
	print(f"You can move to these rooms: \n")

	for item in room.adj_room: 
		print(f"\t{item}\n")
	

	if room.ingredients or room.weapons:
		print(f"you can see these items: \n")
		
		if room.ingredients:
			for ingredient in room.ingredients: 
				print(f"\t{ingredient.ing_id}\n")
		
		if room.weapons: 
			for weapon in room.weapons: 
				print(f"\t{weapon.weapon_id}")


	user_input = input(">>> ").lower()
	
	user_input = user_input.strip() 

	user_input = re.compile('\w+').findall(user_input)

	if "go" in user_input:
		for word in user_input: 
			if word in room.adj_room: 
				player.current_room = rooms[word]
				break 

	if "pickup" in user_input:
		for word in user_input: 
			if word in room.ingredients: 
				player.ingredients.append(ingredients[word])
				break
			elif word in room.weapons: 
				player.weapons.append(weapons[word])
				break


def main():
	title_screen(xedi_list)

	while True:
		normal_room(player.current_room, player)


if __name__ == "__main__":
	main()