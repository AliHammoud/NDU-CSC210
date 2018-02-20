class Mover:
    def __init__(self):
        self.location = PVector(random(width), random(height))
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.top_speed = 1.5
        
        self.angle = 0
        
         #mouse is a private variable (set using trailing double underscores)  
        __mouse = PVector(0, 0)
        self.dir = PVector(0, 0)
        
        self.color = 255
        self.alpha = 20
        
    def update(self):
        
        __mouse = PVector(mouseX, mouseY)
        self.dir = PVector.sub(__mouse, self.location)
        
        self.dir.normalize()
        self.dir.mult(0.05)
        
        self.acceleration = self.dir
        
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.top_speed)
        self.location.add(self.velocity)
        
    def display(self):
        stroke(255, self.velocity.mag() / 2)
        fill(self.color, self.alpha)
        
        rectMode(CENTER)
        
        #self.angle = tan(self.velocity.y / self.velocity.x
        #self.angle = atan2(self.velocity.y, self.velocity.x)
        self.angle = self.velocity.heading()
        
        pushMatrix()
        
        translate(self.location.x, self.location.y)
        rotate(self.angle)
        
        rect(0, 0, 30, 60)
        
        popMatrix()
        
    def checkEdges(self):
        if self.location.x > width:
            self.location.x = 0
        elif self.location.x < 0:
            self.location. x = width
            
        if self.location.y > height:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = height

#init a list with 20 zeros
movers = []
MAX_MOVERS = 1
            
def setup():
    size (640, 360)
    
    global movers, MAX_MOVERS
    
    print(movers)
    
    for index in range(MAX_MOVERS):
        movers.append(Mover())
        
    background(0)
    
def draw():
    
    for mover in movers:
        mover.update()
        mover.checkEdges()
        mover.display()
    