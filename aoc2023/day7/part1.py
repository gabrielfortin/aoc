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

print(data)
print(mapadou("HH2777"))
print(rev("HH2777"))

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
        ranking_dict[handtype].append(hand)
        return
    splitting_index = 0
    for i in range(len(ranking_dict[handtype])):
        ranked_hand = ranking_dict[handtype][i]
        comparison_winner = whichIsHigher(hand, ranked_hand)
        if comparison_winner == hand:
            splitting_index = i
            break
    ranking_dict[handtype] = ranking_dict[handtype][0:i] + [hand] + ranking_dict[handtype][i:-1]

for entry in data:
    hand = entry.split(" ")[0]
    print(hand)
    rez = rev(hand)
    mapp = mapadou(hand)
    if rez.get(5):
        print("five of a kind")
        rank(hand, "five of a kind")
    elif rez.get(4):
        print("four of a kind")
        rank(hand, "four of a kind")
    elif len(mapp.values()) == 2:
        print("full house")
        rank(hand, "full house")
    elif rez.get(3) and len(mapp.values()) == 3:
        print("three of a kind")
        rank(hand, "three of a kind")
    elif len(mapp.values()) == 3 and rez.get(2) and rez.get(1):
        print("two pairs")
        rank(hand, "two pairs")
    elif rez.get(2) and rez.get(1) and len(mapp.values()) == 4:
        print("one pair")
        rank(hand, "one pair")
    elif len(mapp.values()) == 5:
        print("high card")
        rank(hand, "high card")

print(ranking_dict)