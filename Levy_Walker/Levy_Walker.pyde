class Walker:
    
    def __init__(self):
        self.x = width/2
        self.y = height/2
        self.step_size = 5 # Stylize our output
        
    def display(self, prev_x, prev_y, cur_x, cur_y):
        stroke(255)
        line(cur_x, cur_y, prev_x, prev_y)
        
    def step(self):
        #floating point random produces all possible values in [-1, 1]
        rand = random(1)
        
        if rand < 0.01:
            stepX = random(-20, 20)
            stepY = random(-20, 20)
        else:
            stepX = random(-1, 1)
            stepY = random(-1, 1)
            
        self.display(self.x, self.y, self.x + stepX * self.step_size, self.y + stepY * self.step_size)
                     
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