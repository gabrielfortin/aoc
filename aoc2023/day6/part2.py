import re
with open("input.txt", "r") as f:
    data = f.read()
        
def part2():
    lines = data.split("\n")
    duration = int("".join(re.findall("\d+", lines[0])))
    record = int("".join(re.findall("\d+", lines[1])))
    return sum([((speed * (duration - speed)) > record) for speed in list(range(duration + 1))])

print(part2())

