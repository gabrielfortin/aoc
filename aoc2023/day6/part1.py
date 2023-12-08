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
        
class Races:
    def __init__(self, data):
        lines = data.split("\n")
        durations = re.findall("\d+", lines[0])
        records = re.findall("\d+", lines[1])
        self.races = [Race(durations[i], records[i]) for i in range(len(durations)) ]
    
    def part1(self):
        result = 1
        for race in self.races:
            result *= race.simulate_all_races()
        return result

r = Races(data)
print(r.part1())

