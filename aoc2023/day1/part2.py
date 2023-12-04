import re

# CONSTANTS
numbers = ["1","2","3","4","5","6","7","8","9","0"]
numbers_char = {
    3: ["one","two","six"],
    4: ["four","five","nine"],
    5: ["three","seven","eight"]
}
mapping = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

# CODE
inputdata = list()
with open("input.txt", "r") as f:
    inputdata = f.readlines()

def findCharNum(line, i, number):
    char = line[i]
    if char in [c[0] for c in numbers_char[number]] and i+number < len(line) and line[i:i+number] in numbers_char[number]:
        return mapping[line[i:i+number]]
    return None

def findCalibrationForLine(line):
    first_number = None
    last_number = None
    for i in range(len(line)):
        number = None
        char = line[i]
        if char in numbers:
            number = char
        else:
            number = findCharNum(line,i,3)
            number = findCharNum(line,i,4) if findCharNum(line,i,4) is not None else number
            number = findCharNum(line,i,5) if findCharNum(line,i,5) is not None else number
            
        if number is not None:
            if first_number is None:
                first_number = number
            last_number = number

    return int(str(first_number) + str(last_number))

print(sum([findCalibrationForLine(line) for line in inputdata]))