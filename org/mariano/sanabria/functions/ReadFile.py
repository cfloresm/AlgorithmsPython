#Modulo ReadFile.py
def readFileNumbers():
	theFile = open("files/numbers.sort", "r")
	theInts = []
	for val in theFile.read().split():
		theInts.append(int(val))
		theFile.close()
	return theInts


