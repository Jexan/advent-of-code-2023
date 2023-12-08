paths = {}
instructions = None
        

def decode_lines(line: str):
    global instructions
    
    if "=" in line:
        node_name, node_poss = line.split(" = ")
        node_a, node_b = node_poss.replace("(", "").replace(")", "").split(", ")
        paths[node_name] = (node_a, node_b.strip())
    elif len(line) > 2:
        instructions = line.strip()


def follow_path(starting_node="AAA", n_steps=0):
    current_node = starting_node
    
    for l in instructions:
        if l == "L":
            current_node = paths[current_node][0]
        else:
            current_node = paths[current_node][1]
        n_steps += 1
        
        if current_node == "ZZZ":
            return n_steps
    else:
        return follow_path(current_node, n_steps)
    
        
        
def decode_message():
    with open("input1.txt") as f:
        for l in f.readlines():
            decode_lines(l)
     
    print(instructions)
    print(paths)       
    return follow_path()
            
            
result = decode_message()
print(result)