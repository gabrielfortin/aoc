import re

inputdata = list()
with open("input.txt", "r") as f:
    inputdata = f.readlines()

def findCalibrationForLine(line):
    digits = re.findall("\d", line)
    return int(digits[0] + digits[-1])

print(sum([findCalibrationForLine(line) for line in inputdata]))