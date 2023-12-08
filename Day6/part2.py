distances = []
durations = []

def product(iterator):
    total = 1
    for i in iterator:
        total *= i
        
    return total
        

def decode_lines(line: str):
    _, numbers_row = line.split(":")
    real_num = "".join(numbers_row.split())
    
    if "Time" in line:    
        durations.append(int(real_num))
    else:
        distances.append(int(real_num))


def possibilities(races):
    for time, distance in races:
        count = 0
        for i in range(time):
            distance_travelled = i*(time - i)
            if distance_travelled > distance:
                count += 1
                
        yield count
        
        
def decode_message():
    with open("input1.txt") as f:
        for l in f.readlines():
            decode_lines(l)
            
    return product(possibilities(zip(durations, distances)))
            
            
result = decode_message()
print(result)