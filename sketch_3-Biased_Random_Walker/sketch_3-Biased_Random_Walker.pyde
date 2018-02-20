class Walker:
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.step_size = 1 # Stylize our output
        
    def display(self):
        stroke(255)
        point(self.x, self.y)
        
    def step(self):
        
        prob = random(1)
        
        if (prob <= 0.6): #60% probability to go right
            self.x += 1 * self.step_size
            
        elif (prob <= 0.8): #20% probability to go left
            self.x -= 1 * self.step_size
            
        elif (prob <= 0.9): #10% probability to go up
            self.y += 1 * self.step_size
            
        elif (prob <= 1): #10% probability to go down
            self.y -= 1 * self.step_size

def setup():
    
    size(512,512)
    background(0)
    
    global w 
    w = Walker()
    
def draw():
    w.step()
    w.display()