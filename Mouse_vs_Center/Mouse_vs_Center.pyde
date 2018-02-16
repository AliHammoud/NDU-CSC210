class PVector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(self, b):
        self.x += b.x
        self.y += b.y
        
    def sub(self, b):
        self.x -= b.x
        self.y -= b.y
        
    def mult(self, val):
        self.x *= val
        self.y *= val
        
    def div(self, val):
        self.x *= val
        self.y *= val
    
    def mag(self):
        return sqrt(self.x * self.x + self.y * self.y)
        
center = PVector(0, 0)
mouse = PVector(0, 0)
    
def setup():
    size (512, 512)
    background (0)

def draw():
    
    global center
    global mouse
    center = PVector(width/2, height/2)
    mouse = PVector(mouseX, mouseY)
    mouse.sub(center)

    translate(width/2, height/2)

    stroke(noise(mouseX) * 255, noise(mouseY) * 255, noise(center.x) * 255, random(255))
    line(0, 0, mouse.x, mouse.y)
    
    

    