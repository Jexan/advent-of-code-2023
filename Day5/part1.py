from collections import namedtuple

maps = {}
current_map = None
seeds = []
mapping = namedtuple("Mapping", ["output", "input", "n_value"])

def decode_ranges(line: str):
    global current_map
    
    if "seeds:" in line:
        _, seeds_range = line.split(":")
        seeds_ints = map(int, seeds_range.split())
        seeds.extend(seeds_ints) 
    elif "map" in line:
        map_name, _ = line.split(" ")
        current_map = map_name
        maps[map_name] = []
    elif len(line) > 2:
        output, _input, n_value = map(int, line.split())
        maps[current_map].append(mapping(output, _input, n_value))
        
def get_locations(seeds: list[int]):
    for seed in seeds:
        current_value = seed
        for v in maps.values():
            for translation in v:
                if translation.input <= current_value < translation.input + translation.n_value:
                    n_steps = current_value - translation.input
                    current_value = translation.output + n_steps
                    break
                
        yield current_value

def decode_message():
    with open("input1.txt") as f:
        for l in f.readlines():
            decode_ranges(l)
            
    for v in maps.values():
        v.sort(key=lambda x: x.input)
        
    return min(get_locations(seeds))
            
result = decode_message()
print(result)