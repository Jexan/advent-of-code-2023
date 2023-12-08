from collections import namedtuple
import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def decode_lines(line: str):
    line_info = {
        "id": 0,
        "green": set(),
        "red": set(),
        "blue": set()
    }
    
    id_match = re.search("Game (\d+)", line)
    line_info["id"] = id_match.group(1)
    
    for ball_set in line[id_match.end() + 1:].split(";"):
        for type_of_ball in ball_set.split(","):
            number, color = type_of_ball.split()
            line_info[color].add(int(number))
           
    return line_info        
        
        
def decode_message():
    total = 0
    with open("input1.txt") as f:
        for line_decoded in map(decode_lines, f.readlines()):
            total += max(line_decoded["red"])*max(line_decoded["green"])*max(line_decoded["blue"])
            
    return total
            
            
print(decode_message())        