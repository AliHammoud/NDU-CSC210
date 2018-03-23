import copy
import random

#ruleset = [0, 1, 0, 1, 1, 0, 1, 0]
ruleset = [random.randint(0,1) for num in range(8)]

#cells = [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
#cells = [1] * 512
cells = [random.randint(0,1) for num in range(512)]

new_cells = []

background(0)
noStroke()
c_width = 2
size(512, 512)
epochs = 256

def rules(a, b, c):
    
    #Legible, but redundant way of creating the rules:
    '''
    if   a == 1 and b == 1 and c == 1: return ruleset[0]
    elif a == 1 and b == 1 and c == 0: return ruleset[1]
    elif a == 1 and b == 0 and c == 1: return ruleset[2]
    elif a == 1 and b == 0 and c == 0: return ruleset[3]
    elif a == 0 and b == 1 and c == 1: return ruleset[4]
    elif a == 0 and b == 1 and c == 0: return ruleset[5]
    elif a == 0 and b == 0 and c == 1: return ruleset[6]
    elif a == 0 and b == 0 and c == 0: return ruleset[7]
    '''
    
    #DRY but not-so-legible way:
    #concatenate all the input into a binary string (3-bits)
    #decode the binary string into a number
    #return a rule with the index of the decoded binary string
    
    return(ruleset[int(str(a) + str(b) + str(c), 2)])

for x in range(epochs):
    
    new_cells.append(cells[0])
    
    for i in range(len(cells)):
        if cells[i] == 1: 
            #fill(255)
            fill(int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
        else:
            fill(0)
            
        rect(i * c_width, c_width * x, c_width, c_width)
    
    for i in range(1, len(cells) - 1):
        left = cells[i - 1]
        middle = cells[i]
        right = cells[i + 1]
        
        new_state = rules(left, middle, right)
        new_cells.append(new_state)
    
    new_cells.append(cells[-1])
    
    cells = copy.deepcopy(new_cells)
    new_cells = []