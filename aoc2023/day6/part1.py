import re
with open("inputtest.txt", "r") as f:
    data = f.read()

class Race:
    def __init__(self, duration, record):
        self.duration = int(duration)
        self.record = int(record)
    
    def __repr__(self):
        return f"duration : {self.duration}, record : {self.record}"

    def run_race(self, speed):
        distance = speed * (self.duration - speed)
        return distance > self.record

    def simulate_all_races(self):
        speeds = list(range(self.duration + 1))
        # print([self.run_race(speed) for speed in speeds])
        num_of_won = sum([self.run_race(speed) for speed in speeds])
        print(num_of_won)
        return num_of_won
        
            

class Races:
    def __init__(self, data):
        lines = data.split("\n")
        durations = re.findall("\d+", lines[0])
        records = re.findall("\d+", lines[1])
        races = list()

        for i in range(len(durations)):
            race = Race(durations[i], records[i])
            races.append(race)
        
        self.races = races
    
    def part1(self):
        result = 1
        for race in self.races:
            result *= race.simulate_all_races()
        print(result)



r = Races(data)
r.part1()

