class Mover:
    def __init__(self):
        self.position = PVector(width/4, height/4)
        self.velocity = PVector()
        self.acceleration = PVector(1, 0)
        self.mass = 1
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.acceleration.mult(0)
        
    def display(self):
        fill(255, 5)
        noStroke()
        ellipse(self.position.x, self.position.y, 10, 10)
        
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