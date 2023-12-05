with open("input.txt", "r") as f:
    games = f.readlines()

d = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def gameid_if_game_possible(game):
    game_id = game.split(":")[0].strip("Game ")
    game_data = game.split(":")[-1].strip()
    rounds = [[item.strip() for item in round.split(",")] for round in game_data.split(";")]
    for round in rounds:
        for hand in round:
            if int(hand.split(" ")[0]) > d[hand.split(" ")[1]]:
                return 0
    return int(game_id)

print(sum([gameid_if_game_possible(game) for game in games]))