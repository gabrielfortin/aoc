with open("input.txt", "r") as f:
    data = [i.strip() for i in f.readlines()]

ranking = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

class Hand:
    def __init__(self, entry):
        self.hand = entry.split(" ")[0]
        self.bid = int(entry.split(" ")[1])

    def __repr__(self):
        return f"hand {self.hand} / bid {self.bid}"

def mapadou(hand):
    rez = dict()
    for char in hand:
        if char not in rez:
            rez[char] = 1
        else:
            rez[char] += 1
    return rez

def rev(hand):
    return {v: k for k, v in mapadou(hand).items()}

ranking_dict = {
    "five of a kind": [],
    "four of a kind": [],
    "full house": [],
    "three of a kind": [],
    "two pairs": [],
    "one pair": [],
    "high card": []
}

def whichIsHigher(newbie, oldie):
    for i in range(len(newbie)):
        if ranking.index(newbie[i]) < ranking.index(oldie[i]):
            return newbie
        else:
            return oldie

def rank(hand, handtype):
    if len(ranking_dict[handtype]) == 0:
        ranking_dict[handtype] = [hand]
        return
    for i in range(len(ranking_dict[handtype])):
        ranked_hand = ranking_dict[handtype][i]
        comparison_winner = whichIsHigher(hand.hand, ranked_hand.hand)
        if comparison_winner == hand.hand:
            ranking_dict[handtype].insert(i, hand)
            return
    ranking_dict[handtype].append(hand)

for entry in data:
    hand = Hand(entry)
    rez = rev(hand.hand)
    mapp = mapadou(hand.hand)
    if rez.get(5):
        rank(hand, "five of a kind")
    elif rez.get(4):
        rank(hand, "four of a kind")
    elif len(mapp.values()) == 2:
        rank(hand, "full house")
    elif rez.get(3) and len(mapp.values()) == 3:
        rank(hand, "three of a kind")
    elif len(mapp.values()) == 3 and rez.get(2) and rez.get(1):
        rank(hand, "two pairs")
    elif rez.get(2) and rez.get(1) and len(mapp.values()) == 4:
        rank(hand, "one pair")
    elif len(mapp.values()) == 5:
        rank(hand, "high card")

# Convert dict to list
ranked_list = ranking_dict["five of a kind"] + ranking_dict["four of a kind"] + ranking_dict["full house"]\
             + ranking_dict["three of a kind"] + ranking_dict["two pairs"] + ranking_dict["one pair"] + ranking_dict["high card"]  

# Parse bids per hand
bids = {line.split(" ")[0]: int(line.split(" ")[1]) for line in data}

# Calculate total sum
somme = 0
i = len(ranked_list)
while (i > 0):
    somme += i * ranked_list[len(ranked_list)-i].bid
    i -= 1

from pprint import pprint
pprint(ranked_list)
pprint(ranking_dict)
print(somme)