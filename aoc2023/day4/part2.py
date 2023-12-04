
class Day4:
	def __init__(self):
		f = open("data1.txt", "r")
		self.data = f.readlines()
		f.close()
		self.cards_instances = dict()
		[self.readCard(card) for card in self.data]
	
	def readCard(self, card):
		card_num = card.split(":")[0].strip("Card").strip()
		self.cards_instances[int(card_num)] = 1

	def parseCard(self, card):

		card_num = card.split(":")[0].strip("Card").strip()
		card_clean = card.split(":")[-1]

		win = [num for num in card_clean.split("|")[0].strip().split(" ") if num != ""]
		play = [num for num in card_clean.split("|")[1].strip().split(" ") if num != ""]
	
		wins = sum([True for num in play if num in win])
		cards_won = [int(card_num) + i for i in range(1, wins+1)]
		
		for card in cards_won:
			self.cards_instances[card] += (1 * self.cards_instances[int(card_num)])
			
	def part2(self):
		[self.parseCard(card) for card in self.data]
		
		return sum([v for k, v in self.cards_instances.items()])

d = Day4()
print(d.part2())