class Mover:
    def __init__(self):
        self.location = PVector(random(width), random(height))
        self.velocity = PVector(random(-2, 2), random(-2, 2))
        self.acceleration = PVector(-0.001, 0.01)
        self.top_speed = 10
        
    def update(self):
        self.acceleration = PVector.random2D()
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
    
def draw():
    background(0)
    mover.update()
    mover.checkEdges()
    mover.display()
    