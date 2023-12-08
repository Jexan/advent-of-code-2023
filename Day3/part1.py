from collections import namedtuple
from itertools import takewhile
import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def decode_lines(line: str):       
    return list(line)


def includes_number(strip: list[str]):
    for c in strip:
        if c not in ('.', '\n') and not c.isdigit():
            return True

        
def find_part_numbers(grid: list[str]):
    for line_n, line in enumerate(grid):
        for i, j in enumerate(line):
            if j.isdigit():
                digits = list(takewhile(lambda x: x.isdigit(), line[i:]))
                number = int(''.join(digits))
                how_long = len(digits)
                end_pos = i + how_long
                line[i: end_pos] = ['.']*how_long
                
                if i > 0 and line[i - 1] != '.':
                    yield number 
                    continue
                
                if end_pos < len(line) and line[end_pos] not in ('.', "\n"):
                    yield number
                    continue
                
                if line_n > 0:
                    if includes_number(grid[line_n - 1][max(i - 1, 0): min(end_pos + 1, len(line))]):
                        yield number
                        continue
                    
                if line_n + 1 < len(grid):
                    if includes_number(grid[line_n + 1][max(i - 1, 0): min(end_pos + 1, len(line))]):
                        yield number
                        continue
                    
                    
        
def decode_message():
    with open("input1.txt") as f:
        final_message = [decode_lines(l) for l in f.readlines()]
        
    part_numbers = list(find_part_numbers(final_message))
    print(part_numbers)
            
    return sum(part_numbers)
            
            
            
            
print(decode_message())        
#result = decode_message()
#print(result)