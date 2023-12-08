def decode_numbers(line: str):
    _, two_sets_numbers = line.split(":")
    
    winning_numbers, avail_numbers = two_sets_numbers.split("|")
    
    return set(winning_numbers.split()), set(avail_numbers.split())


def winning_number_value(l: str):
    winning_numbers, available_numbers = decode_numbers(l)
    
    w_numbers = len(winning_numbers & available_numbers)
    
    if w_numbers:
        return 2**(w_numbers-1)
    else:
        return 0


def decode_message():
    with open("input1.txt") as f:
        return sum(winning_number_value(l) for l in f.readlines())
            
            
result = decode_message()
print(result)