from itertools import starmap, pairwise
import operator

numbers = []

def decode_lines(line: str):
    curent_numbers = list(map(int, line.split()))
    numbers.append([curent_numbers])


def get_diffs(listing):
    return list(starmap(operator.sub, pairwise(listing)))
        

def extrapolate(num_list):
    for i, nums in enumerate(num_list[-2::-1], 1):
        nums.append(nums[-1] - num_list[-i][-1])
        
    return num_list[0][-1]
        
def decode_message():
    with open("input.txt") as f:
        for l in f.readlines():
            decode_lines(l)
     
    for num_list in numbers:
        current = num_list[0]
        while any(current):
            current = get_diffs(current)
            num_list.append(current)
        
    total = sum(extrapolate(nums) for nums in numbers)
    return total
        
            
result = decode_message()
print(result)