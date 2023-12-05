from typing import Tuple, List
import re

with open("data.txt", "r") as f:
    schema = f.readlines()

numbers = ["1","2","3","4","5","6","7","8","9","0"]
junk = [".", "\n"]


def build_num(i, j):
    number = schema[i][j]
    for x in range(1, 4):
        if x < len(schema[i]) and schema[i][j+x] in numbers:
            number += schema[i][j+x]
        else:
            break
    return number

def is_symbol(i, j):
    return schema[i][j] not in numbers + junk

def symbol_around_number(i, j, number_len):
    x = -1
    while(x <= number_len):
        for y in [-1, 0, 1]:
            if i+y < len(schema) and j+x < len(schema[i+y]) and is_symbol(i+y, j+x):
                return True
        x += 1
    return False

sum = 0
for i in range(len(schema)):
    j = 0
    while j < len(schema[i]):
        if schema[i][j] in numbers:
            number = build_num(i, j)
            if symbol_around_number(i, j, len(number)):
                sum += int(number)
            j += len(number)
        j += 1
            
        
print(f"sum : {sum}")