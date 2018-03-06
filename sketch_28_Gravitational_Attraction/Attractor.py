class Attractor:
    def __init__(self):
        self.mass = 20
        self.position = PVector(width/2, height/2)
        self.G = 0.4 #gravitational constant
        self.t = 0
        
    def attract(self, mover):
        force = PVector.sub(self.position, mover.position)
        distance = force.mag()
        distance = constrain(distance, 5, 25)
        
        force.normalize()
        pull_strength = (self.G * self.mass * mover.mass) / distance ** 2
        
        force.mult(pull_strength)
        return force
    
    def display(self):
        self.t += 0.001
        
        noStroke()
        fill(sin(self.t) * 255)
        ellipse(self.position.x, self.position.y, self.mass * 2, self.mass * 2)
        
        
        