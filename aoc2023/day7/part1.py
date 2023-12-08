with open("inputtest.txt", "r") as f:
    data = [i.strip() for i in f.readlines()]

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

for entry in data:
    hand = entry.split(" ")[0]
    print(hand)
    rez = rev(hand)
    mapp = mapadou(hand)
    if rez.get(5):
        print("five of a kind")
    elif rez.get(4):
        print("four of a kind")
    elif len(mapp.values()) == 2:
        print("full house")
    elif rez.get(3) and len(mapp.values()) == 3:
        print("three of a kind")
    elif len(mapp.values()) == 3 and rez.get(2) and rez.get(1):
        print("two pairs")
    elif rez.get(2) and rez.get(1) and len(mapp.values()) == 4:
        print("one pair")
    elif len(mapp.values()) == 5:
        print("high card")