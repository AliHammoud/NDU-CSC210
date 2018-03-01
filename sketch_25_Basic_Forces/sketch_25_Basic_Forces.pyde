class PhysicalWalker:
    def __init__(self):
        self.position = PVector(width/2, height/2)
        self.velocity = PVector()
        self.acceleration = PVector()
        self.mass = random(10)
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        
    def display(self):
        fill(255)
        stroke(255)
        ellipse(self.position.x, self.position.y, 20, 20)
        
    def add_force(self, force):
        f = force.get()
        f.div(self.mass)
        self.acceleration.add(f)
        
    def check_edges(self):
        if self.position.x > width:
            self.position.x = width
            self.velocity.x *= -1
        elif self.position.x < 0:
            self.velocity.x *= -1
            self.position.x = 0
            
        if self.position.y > height:
            self.velocity.y *= -1
            self.position.y = height
            

def setup():
    size(512, 512)
    global object, wind, gravity
    object = PhysicalWalker()
    wind = PVector(0.5, 0)
    gravity = PVector(0, 2)
    
def draw():
    background(0)

    if mousePressed:
        object.add_force(wind)
    
    object.add_force(gravity)
    object.update()
    object.check_edges()
    object.display()
    print(wind)