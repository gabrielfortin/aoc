from typing import List

with open("input.txt", "r") as f:
    data = f.read()

def format_mat(entry_name):
    d = data.split(entry_name)[-1].strip().split("\n\n")[0].split("\n")
    return {int(i.split(" ")[1]): {"entry": int(i.split(" ")[1]), 
                                   "dest": int(i.split(" ")[0]), 
                                   "len": int(i.split(" ")[2])} for i in d}

first = format_mat("seed-to-soil map:")
sec = format_mat("soil-to-fertilizer map:")
tr = format_mat("fertilizer-to-water map:")
fo = format_mat("water-to-light map:")
fi = format_mat("light-to-temperature map:")
si = format_mat("temperature-to-humidity map:")
sev = format_mat("humidity-to-location map:")


def solve_step(entry, matrix):
    for mat in matrix.values():
        if entry >= mat["entry"] and entry < (mat["entry"] + mat["len"]):
            return mat["dest"] + (entry - mat["entry"])

    return entry

seeds = [int(i) for i in data.split("\n\n")[0].split("seeds: ")[-1].split(" ")]

res = list()
for seed in seeds:
    r = solve_step(seed, first)
    r = solve_step(r, sec)
    r = solve_step(r, tr)
    r = solve_step(r, fo)
    r = solve_step(r, fi)
    r = solve_step(r, si)
    r = solve_step(r, sev)
    res.append(r)
    # print(f"res {r}")

print(min(res))