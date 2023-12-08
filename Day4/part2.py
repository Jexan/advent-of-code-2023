def decode_numbers(line: str):
    _, two_sets_numbers = line.split(":")
    
    winning_numbers, avail_numbers = two_sets_numbers.split("|")
    
    return set(winning_numbers.split()), set(avail_numbers.split())


def winning_number_value(l: str, i: int):
    winning_numbers, available_numbers = decode_numbers(l)
    
    w_numbers = len(winning_numbers & available_numbers)
    
    for j in range(i + 1, i + 1 + w_numbers):
        TOTALS[j] += TOTALS[i]
        
    return TOTALS[i]
    


def decode_message():
    with open("input1.txt") as f:
        return sum(winning_number_value(l, i) for i, l in enumerate(f.readlines()))
            
from collections import defaultdict
TOTALS = defaultdict(lambda: 1)
     
result = decode_message()
print(result)