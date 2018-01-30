class Walker:
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.step_size = 1 # Stylize our output
        self.prob = random(1)
        
    def display(self):
        stroke(255)
        point(self.x, self.y)
        
    def step(self):
        
        self.prob = random(1)
        
        if (self.prob <= 0.25): #25% probability to go right
            self.x += 1 * self.step_size
            print('right')
            
        elif (self.prob <= 0.5): #25% probability to go left
            self.x -= 1 * self.step_size
            print('left')
            
        elif (self.prob <= 0.75): #25% probability to go up
            self.y += 1 * self.step_size
            print('up')
            
        elif (self.prob <= 1): #25% probability to go down
            self.y -= 1 * self.step_size
            print('down')
            
        print('')

def setup():
    
    size(512,512)
    background(0)
    
    global w 
    w = Walker()
    
def draw():
    w.step()
    w.display()
    
def keyPressed():
    if (key == 'w'):
        #do something
        
    elif (key == 'a'):
        #do something
        
    elif (key == 's'):
        #do something
        
    elif (key == 'd'):
        #do something