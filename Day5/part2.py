from collections import namedtuple

maps = {}
current_map = None
seeds = []

mapping = namedtuple("Mapping", ["begin_interval", "b"])
interval = namedtuple("Seed", ["initial_value", "final_value"])

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
        maps[current_map].append(mapping(interval(_input, _input + n_value - 1), output - _input))
     

def null_interval(a: interval):
    return a.initial_value >= a.final_value
     
     
def split_by_overlap(a: interval, b: interval):
    return (
        interval(a.initial_value, b.initial_value - 1), 
        interval(max(a.initial_value, b.initial_value), min(a.final_value, b.final_value)),
        interval(b.final_value + 1, a.final_value)
    )
    
    
def transform_interval(a: interval, f: mapping):
    return interval(a.initial_value + f.b, a.final_value + f.b)
    
    
def expand_locations(seeds: list[interval], map_values: list[mapping]):
    for seed in seeds:
        for f in map_values:
            left_end, overlapping_interval, right_end = split_by_overlap(seed, f.begin_interval)
            if null_interval(overlapping_interval):
                continue
            
            yield transform_interval(overlapping_interval, f)
            
            if not null_interval(left_end):
                print(seed, f, left_end, overlapping_interval, right_end)
                seeds.append(left_end)
            if not null_interval(right_end):
                print(seed, f, left_end, overlapping_interval, right_end)
                seeds.append(right_end)
                
            break
        else:
            yield seed


def batched(xs, n):
    xs = iter(xs)
    
    while True:
        current = n
        batch = []
        
        for x in xs:
            batch.append(x)
            current -= 1
            
            if not current:
                yield batch
                break
        else:
            break
    

def transform_seed_range(seeds):
    for start, n_seeds in batched(seeds, 2):
        yield interval(start, start + n_seeds - 1)


def decode_message():
    with open("input1.txt") as f:
        for l in f.readlines():
            decode_ranges(l)
            
    current_seeds = list(transform_seed_range(seeds))
    for v in maps.values():
        current_seeds = list(expand_locations(current_seeds, v))
        
        
    print(min(current_seeds, key=lambda x: x.initial_value))
            
result = decode_message()
print(result)