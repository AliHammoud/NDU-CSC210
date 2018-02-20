class Walker:
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        
    def display(self):
        stroke(255)
        point(self.x, self.y)
        
    def step(self):
        choice = int(random(4))
        
        if (choice == 0): self.x += 1
        elif (choice == 1): self.x -= 1
        elif (choice == 2): self.y += 1
        else: self.y -= 1

def setup():
    
    size(512,512)
    background(0)
    
    global w 
    w = Walker()
    
def draw():
    w.step()
    w.display()