import copy
import random

size(512, 512)

c_width = 64
epochs = width/c_width
ruleset = [random.randint(0,1) for num in range(8)]
cells = [random.randint(0,1) for num in range(8)]

new_cells = []

background(0)
noStroke()

def rules(a, b, c):
    
    return(ruleset[int(str(a) + str(b) + str(c), 2)])

for x in range(epochs):
    
    new_cells.append(cells[0])
    
    for i in range(len(cells)):
        if cells[i] == 1: 
            fill(255)
            #fill(int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)), int(random.randint(0, 255)))
        else:
            fill(0)
            
        rect(i * c_width, c_width * x, c_width, c_width)
        #ellipse(i * c_width, c_width * x, c_width, c_width)
    
    for i in range(1, len(cells) - 1):
        left = cells[i - 1]
        middle = cells[i]
        right = cells[i + 1]
        
        new_state = rules(left, middle, right)
        new_cells.append(new_state)
    
    new_cells.append(cells[-1])
    
    cells = copy.deepcopy(new_cells)
    new_cells = []