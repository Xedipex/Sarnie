import time

mylist = ["x", "e", "d", "i", "p", "e", "x"]

for i in range(len(mylist)+1):
	print(' '.join(mylist[:i]))
	#print(mylist[:i])
	time.sleep(0.2)

for i in range(1, len(mylist)+1):
	print(' '.join(mylist[:-i]))
	#print(mylist[:-i])
	time.sleep(0.2)
time.sleep(1)

print("\nX E D I P E X")
time.sleep(1)
print("\n'George Makes a Sandwich'\n")

