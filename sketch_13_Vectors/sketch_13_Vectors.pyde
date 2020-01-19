class PVector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, b):
        self.x += b.x
        self.y += b.y
        
location = PVector(0, 0)
velocity = PVector(3, 5)
    
def setup():
    size (512, 512)
    background (0)
    
    
def draw():
    
    global location
    global velocity
    location.add(velocity)
    
