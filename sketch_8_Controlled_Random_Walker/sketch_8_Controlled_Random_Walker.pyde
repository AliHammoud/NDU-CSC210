class Walker:
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.step_size = 5 # Stylize our output
        
    def display(self):
        stroke(255)
        rect(self.x, self.y, 1, 1)
        
    def step(self):
        
        prob = random(1)
        
        if (prob <= 0.25): #60% probability to go right
            self.x += 1 * self.step_size
            
        elif (prob <= 0.5): #20% probability to go left
            self.x -= 1 * self.step_size
            
        elif (prob <= 0.75): #10% probability to go up
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
    
def keyPressed(self):
    if (key == CODED):
        if (keyCode == DOWN):
            w.y += 1 * w.step_size
        elif(keyCode == UP):
            w.y -= 1 * w.step_size
        elif(keyCode == RIGHT):
            w.x += 1 * w.step_size
        elif(keyCode == LEFT):
            w.x -= 1 * w.step_size