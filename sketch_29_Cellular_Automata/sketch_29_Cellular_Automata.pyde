ruleset = [0, 1, 0, 1, 1, 0, 1, 0]

def rules(a, b, c):
    if a == 1 and b == 1 and c == 1: return ruleset[0]
    elif a == 1 and b == 1 and c == 1: return ruleset[1]
    elif a == 1 and b == 0 and c == 1: return ruleset[2]
    elif a == 1 and b == 0 and c == 1: return ruleset[3]
    elif a == 0 and b == 1 and c == 1: return ruleset[4]
    elif a == 0 and b == 1 and c == 1: return ruleset[5]
    elif a == 0 and b == 0 and c == 1: return ruleset[6]
    elif a == 0 and b == 0 and c == 1: return ruleset[7]
    return 0

cells = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
new_cells = []

for i in range(len(cells)):
    if cells[i] == 0: fill(255)
    else: fill(80)
    
    stroke(60)
           
    rect(i * 50, 0, 50, 50)
    
size(1000, 50)

for i in range(1, len(cells) - 1):
    left = cells[i - 1]
    middle = cells[i]
    right = cells[i + 1]
    
    new_state = rules(left, middle, right)
    new_cells.append(new_state)
    
cells = new_cells