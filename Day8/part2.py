import numpy as np

paths = {}
instructions = None
all_nodes = []        
order_nodes = {}


def decode_lines(line: str):
    global instructions
    
    if "=" in line:
        node_name, node_poss = line.split(" = ")
        node_a, node_b = node_poss.replace("(", "").replace(")", "").split(", ")
        paths[node_name] = (node_a, node_b.strip())
    elif len(line) > 2:
        instructions = line.strip()


def find_beggining_nodes():
    for k in paths:
        if k[-1] == "A":
            all_nodes.append(k)


def find_min_cycle(node):
    order = 0
    current_node = node
    
    while True:
        for l in instructions:
            if l == "L":
                current_node = paths[current_node][0]
            else:
                current_node = paths[current_node][1]
                
            order += 1
            if current_node[-1] == 'Z':
                return order 
        
        
def decode_message():
    with open("input1.txt") as f:
        for l in f.readlines():
            decode_lines(l)
     
    find_beggining_nodes()      
    return np.lcm.reduce(np.array([find_min_cycle(node) for node in all_nodes], dtype=np.int64))
    
            
            
result = decode_message()
print(result)