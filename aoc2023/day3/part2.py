from typing import Tuple, List
import re

with open("data.txt", "r") as f:
    schema = f.readlines()

numbers = ["1","2","3","4","5","6","7","8","9","0"]

symbols = {}


def build_num(i, j):
    number = schema[i][j]
    for x in range(1, 4):
        if x < len(schema[i]) and schema[i][j+x] in numbers:
            number += schema[i][j+x]
        else:
            break
    return number

def symbol_around_number(i, j, number_len, number):
    x = -1
    while(x <= number_len):
        for y in [-1, 0, 1]:
            if i+y < len(schema) and j+x < len(schema[i+y]) and schema[i+y][j+x] not in numbers and schema[i+y][j+x] not in [".", "\n"]:
                symbol = schema[i+y][j+x]
                if symbol == "*":
                    symbolindex = f"{i+y},{j+x}"
                    if symbolindex not in symbols:
                        symbols[symbolindex] = [int(number)]
                    else:
                        symbols[symbolindex].append(int(number))
                return True
        x += 1
    return False

# Batir la table de gears
for i in range(len(schema)):
    j = 0
    while j < len(schema[i]):
        if schema[i][j] in numbers:
            number = build_num(i, j)
            symbol_around_number(i, j, len(number), number)
            j += len(number)
        j += 1
            
# calculer les ratios
sum = 0
for k, v in symbols.items():
    if len(v) == 2:
        ratio = int(v[0]) * int(v[1])
        sum += ratio
print(sum)