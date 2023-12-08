with open("input.txt", "r") as f:
#with open("input_test_p2.txt", "r") as f:
    data = f.readlines()

instruc = data[0].strip()

lines = data[2:]
from pprint import pprint
linesdict = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in lines}

step = 0
depassement = 0
entries = [line[0:3] for line in lines if line[2] == "A"]

results = dict()
for entry in entries:
    depassement = 0
    while(entry[2] < "Z"):
        if len(instruc) == step:
            step = 0
            depassement += 1
        leftright = instruc[step]

        entry = linesdict[entry][leftright]
        
        print(step + (step*depassement))
        step += 1
    results[entry] = (step + (step*depassement) - 1)

print(results)

step = step + depassement * step

'''
muls = list()
for k1, v1 in results.items():
    for k2, v2 in results.items():
        if k1 != k2:
            muls.append(v1*v2)
'''

muls = len(instruc)*sum(results.values())
print(f"reponse {muls}")
