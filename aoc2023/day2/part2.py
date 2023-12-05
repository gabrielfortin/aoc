with open("input.txt", "r") as f:
    games = f.readlines()

def gamePower(game):
    max = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    game_data = game.split(":")[-1].strip()
    rounds = [[item.strip() for item in round.split(",")] for round in game_data.split(";")]
    for round in rounds:
        for hand in round:
            if int(hand.split(" ")[0]) > max[hand.split(" ")[1]]:
                max[hand.split(" ")[1]] = int(hand.split(" ")[0])
    return max["red"] * max["green"] * max["blue"]

print(sum([gamePower(game) for game in games]))