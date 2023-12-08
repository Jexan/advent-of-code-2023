from collections import namedtuple

digits_dict = {
    "one": "1  ",
    "two": "2  ",
    "three": "3    ",
    "four": "4   ",
    "five": "5   ",
    "six": "6  ",
    "seven": "7    ",
    "eight": "8    ",
    "nine": "9   "
}


digit_pos = namedtuple("DigitPos", ["index", "value"])


def decode_number(line: str):
    possible = []
    for str_digit, int_digit in digits_dict.items():
        possible.append(line.replace(str_digit, int_digit))
        
    min_digit = digit_pos(float("inf"), 0)
    max_digit = digit_pos(-1, 0)
    
    for s in possible:
        for index, c in enumerate(s):
            if c.isdigit():
                if min_digit.index > index:
                    min_digit = digit_pos(index, int(c))
                if max_digit.index < index:
                    max_digit = digit_pos(index, int(c))
            
    return min_digit.value*10 + max_digit.value
        

def decode_message():
    with open("input1.txt") as f:
        return sum(decode_number(l) for l in f.readlines())
            
            
result = decode_message()
print(result)