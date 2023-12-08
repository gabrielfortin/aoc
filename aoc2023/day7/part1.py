with open("inputtest.txt", "r") as f:
    data = [i.strip() for i in f.readlines()]

ranking = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

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
        comparison_winner = whichIsHigher(hand, ranked_hand)
        if comparison_winner == hand:
            ranking_dict[handtype].insert(i, hand)
            return
    ranking_dict[handtype].append(hand)

for entry in data:
    hand = entry.split(" ")[0]
    rez = rev(hand)
    mapp = mapadou(hand)
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

ranked_list = list()
for k,v in ranking_dict.items():
    ranked_list += v

bids = {line.split(" ")[0]: int(line.split(" ")[1]) for line in data}

# total
somme = 0
i = len(ranked_list)
while (i > 0):
    somme += i * bids[ranked_list[len(ranked_list)-i]]
    i -= 1
print(somme)