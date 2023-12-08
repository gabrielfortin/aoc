with open("input.txt", "r") as f:
    data = f.readlines()

instruc = data[0].strip()

lines = data[2:-1]
from pprint import pprint
linesdict = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in lines}

step = 0
depassement = 0
entry = "AAA"
while(entry != "ZZZ"):
    if len(instruc) == step:
        step = 0
        depassement += 1
    leftright = instruc[step]
    entry = linesdict[entry][leftright]
    step += 1


step = step + depassement * step
print(step)