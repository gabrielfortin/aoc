import re
with open("input.txt", "r") as f:
    data = f.read()

class Race:
    def __init__(self, duration, record):
        self.duration = int(duration)
        self.record = int(record)

    def simulate_all_races(self):
        speeds = list(range(self.duration + 1))
        num_of_won = sum([((speed * (self.duration - speed)) > self.record) for speed in speeds])
        return num_of_won
        
def part1():
    lines = data.split("\n")
    durations = re.findall("\d+", lines[0])
    records = re.findall("\d+", lines[1])
    result = 1
    for race in [Race(durations[i], records[i]) for i in range(len(durations)) ]:
        result *= race.simulate_all_races()
    return result

print(part1())

