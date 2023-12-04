import re

def findCalibrationForLine(line):
    digits = re.findall("\d", line)
    return int(digits[0] + digits[-1])
    
with open("input.txt", "r") as f:
	print(sum([findCalibrationForLine(line) for line in f.readlines()]))