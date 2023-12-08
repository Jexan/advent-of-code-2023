def decode_number(line: str):
    digits = []
    for i in line:
        if i.isdigit():
            digits.append(int(i))
            
    return digits[0]*10 + digits[-1]
        
def decode_message():
    with open("input1.txt") as f:
        return sum(decode_number(l) for l in f.readlines())
            
            
result = decode_message()
print(result)