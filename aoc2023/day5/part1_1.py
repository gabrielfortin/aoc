from typing import List

with open("input.txt", "r") as f:
    data = f.read()

class Map:
    def __init__(self, data):
        dest_range_start = int(data.split(" ")[0])
        src_range_start = int(data.split(" ")[1])
        range_len = int(data.split(" ")[2])
        self.range_len = range_len
        self.src_range = list(range(src_range_start, src_range_start+range_len))
        self.dest_range = list(range(dest_range_start, dest_range_start+range_len))

    def __str__(self):
        return f"src range : {self.src_range}  |  dest range {self.dest_range}"

    def __repr__(self):
        return str(self)

    @property
    def mapping(self):
        return {self.src_range[i] : self.dest_range[i] for i in range(self.range_len)}

class Mapping:
    def __init__(self, data):
        self._from = data.split("-")[0].strip()
        self._to = data.split("-")[2].split(" ")[0].strip()
        self._data = data.split("map:")[-1].strip().split("\n")
        # print(self._from, self._to, self._data)
    @property
    def maps(self) -> dict:
        # return [Map(data) for data in self._data]
        big_map = dict()
        for data in self._data:
            big_map.update(Map(data).mapping)
        return big_map

class Problem:
    def __init__(self, data):
        self._data = data
        self.mappings = [Mapping(entry) for entry in data.split("\n\n")[1:]]

    def solve(self):
        seeds = [int(i) for i in self._data.split("\n\n")[0].strip().split(" ")[1:]]
        print(seeds)
        min_result = 10000000000000

        for seed in seeds:
            rez = self.solve_a_seed(seed)
            if rez < min_result:
                min_result = rez

        return f"minimum : {min_result}"


    def solve_a_seed(self, seed):
        entry = seed
        for mapping in self.mappings:
            #print(entry)
            if entry in mapping.maps:
                entry = mapping.maps[entry]

        return entry
        

if False:
    data = data.split("\n\n")
    mapping = Mapping(data[1])
    print("\n")
    print(mapping.maps[1])
    print(mapping.maps[1].mapping)

p = Problem(data)
print(p.solve())