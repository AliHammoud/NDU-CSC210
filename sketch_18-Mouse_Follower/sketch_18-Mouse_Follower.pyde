class Mover:
    def __init__(self):
        self.location = PVector(random(width), random(height))
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.top_speed = 3
        
         #mouse is a private variable (set using trailing double underscores)  
        __mouse = PVector(0, 0)
        self.dir = PVector(0, 0)
        
    def update(self):
        
        __mouse = PVector(mouseX, mouseY)
        self.dir = PVector.sub(__mouse, self.location)
        
        self.dir.normalize()
        self.dir.mult(0.5)
        
        self.acceleration = self.dir
        self.acceleration.mult(0.15)
        self.acceleration.mult(random(2))
        
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.top_speed)
        self.location.add(self.velocity)
        
    def display(self):
        stroke(0)
        fill(255)
        ellipse(self.location.x, self.location.y, 16, 16)
        
    def checkEdges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location. x = width
            
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height
            
def setup():
    size (640, 360)
    
    global mover
    mover = Mover()
    background(0)
    
def draw():
    mover.update()
    mover.checkEdges()
    mover.display()
    