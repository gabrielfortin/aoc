with open("input.txt", "r") as f:
    data = f.readlines()

instruc = data[0].strip()
print(instruc)


lines = data[2:-1]
lines += lines 
lines += lines
lines += lines
lines += lines
lines += lines
lines += lines
from pprint import pprint
linesdict = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in lines}
pprint(linesdict)

step = 0
depassement = 0
entry = "AAA"
print(len(instruc))
while(entry != "ZZZ"):
    print(step)
    if len(instruc) == step:
        step = 0
        depassement += 1
    leftright = instruc[step]
    entry = linesdict[entry][leftright]
    step += 1


step = step + depassement * step
print(step)