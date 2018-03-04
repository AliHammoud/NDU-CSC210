class RigidBody:
    def __init__(self):
        self.position = PVector(width/2, 50)
        self.velocity = PVector()
        self.acceleration = PVector()
        self.mass = 10
        
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
            
    def is_inside(self, object):
        if self.position.x > object.x \
            and self.position.x < object.x + object.w \
                and self.position.y > object.y \
                    and self.position.y < object.y + object.h:
            return True
        
        else:
            return False
        
    def drag(self, object):
        speed = self.velocity.mag()
        drag_magnitude = object.c * speed * speed
        
        drag = self.velocity.get()
        drag.mult(-1)
        drag.normalize()
        
        drag.mult(drag_magnitude)
        self.add_force(drag)

class Liquid:
    def __init__(self, x, y, w, h, c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        
    def display(self):
        stroke(255)
        fill(255, 30)
        rect(self.x, self.y, self.w, self.h)
        
def setup():
    size(640, 320)
    global liquid, buoy, gravity
    liquid = Liquid(0, height/2, width - 1, height/2 - 1, 0.7)
    buoy = RigidBody()
    gravity = PVector(0, 2)
    
def draw():
    background(0)
    liquid.display()
    
    buoy.add_force(gravity)
    
    if buoy.is_inside(liquid):
        buoy.drag(liquid)
        
        bouyancy = PVector(0, 1.03 * 0.2 * 10)
        buoy.add_force(bouyancy.mult(-1))
    
    buoy.update()
    buoy.check_edges()
    buoy.display()