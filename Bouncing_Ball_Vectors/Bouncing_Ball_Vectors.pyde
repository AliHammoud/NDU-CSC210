class PVector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, b):
        self.x += b.x
        self.y += b.y
        
location = PVector(width/2, height/2)
velocity = PVector(3, 5)
    
def setup():
    size (512, 512)
    background (0)
    
    
def draw():
    
    global location
    global velocity
    
    location.add(velocity)
    
    if location.x > width or location.x < 0:
        velocity.x *= -1
        
    if location.y > height or location.y < 0:
        velocity.y *= -1
        
    fill(255)
    ellipse(location.x, location.y, 10, 10)
    

    