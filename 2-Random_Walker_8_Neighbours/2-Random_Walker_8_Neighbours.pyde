class Walker:
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.step_size = 5 # Stylize our output
        
    def display(self):
        stroke(255)
        point(self.x, self.y)
        
    def step(self):
        '''
        #floating point random produces all possible values in [-1, 1]
        stepX = random(-1, 1)
        stepY = random(-1, 1)
        '''
        
        stepX = int(random(3)) - 1 # produces -1, 0 or 1
        stepY = int(random(3)) - 1
    
        #step is now multiplied by its size to produce a nice effect
        self.x += stepX * self.step_size
        self.y += stepY * self.step_size

def setup():
    
    size(512,512)
    background(0)
    
    global w 
    w = Walker()
    
def draw():
    w.step()
    w.display()