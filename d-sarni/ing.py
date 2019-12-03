
bread = {
	"name": "bread",
	"description": "Tasty bread, essential for a good sandwich, but over-use can lead to dire consequences",
	"SXP": 20
}

def print_stats(bread):

	for keys in bread:
		print(f'{keys}: {bread[keys]}')

print_stats(bread)