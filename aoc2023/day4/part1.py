f = open("data1.txt", "r")
data = f.readlines()
f.close()

def parseCard(card):
	card_clean = card.split(":")[-1]
	win = card_clean.split("|")[0].strip().split(" ")
	win = [num for num in win if num != ""]
	play = card_clean.split("|")[1].strip().split(" ")
	play = [num for num in play if num != ""]
	
	wins = sum([True for num in play if num in win])
	if wins != 0:
		return 2**(wins-1)
	return 0

print(sum([parseCard(card) for card in data]))