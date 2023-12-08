from collections import namedtuple
from itertools import takewhile
import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

class Gear:
    adjacent: list
    
    def __init__(self):
        self.adjacent = []
        
    def product(self):
        print(self.adjacent)
        if len(self.adjacent) == 2:
            return self.adjacent[0] * self.adjacent[1]
        else:
            return 0
        
    def isdigit(self):
        return False


def decode_lines(line: str):       
    return list(line)


def add_to_gears(strip: list[str | Gear], number: int):
    for c in strip:
        if isinstance(c, Gear):
            c.adjacent.append(number)

        
def find_gear_numbers(grid: list[str]):
    for line_n, line in enumerate(grid):
        for i, j in enumerate(line):
            if j.isdigit():
                digits = list(takewhile(lambda x: x.isdigit(), line[i:]))
                number = int(''.join(digits))
                how_long = len(digits)
                end_pos = i + how_long
                line[i: end_pos] = ['.']*how_long
                
                if i > 0 and isinstance(line[i - 1], Gear):
                    line[i - 1].adjacent.append(number)
                
                if end_pos < len(line) and isinstance(line[end_pos], Gear):
                    line[end_pos].adjacent.append(number)
                
                if line_n > 0:
                    add_to_gears(grid[line_n - 1][max(i - 1, 0): min(end_pos + 1, len(line))], number)
                    
                if line_n + 1 < len(grid):
                    add_to_gears(grid[line_n + 1][max(i - 1, 0): min(end_pos + 1, len(line))], number)


gears = []

                    
def replace_for_gears(grid):
    for l_n, l in enumerate(grid):
        for j_n, j in enumerate(l):
            if j == "*":
                current_gear = Gear()
                gears.append(current_gear)
                grid[l_n][j_n] = current_gear
                
    return grid
            
        
def decode_message():
    with open("input1.txt") as f:
        final_message = replace_for_gears([decode_lines(l) for l in f.readlines()])
        
    find_gear_numbers(final_message)
            
    return sum(g.product() for g in gears)
            
                   
print(decode_message())        