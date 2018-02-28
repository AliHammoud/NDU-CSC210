class Oscillator:
    def __init__(self):
        self.angle = PVector()
        self.velocity = PVector(random(-0.2, 0.2), random(-0.2, 0.2))
        self.amplitude = PVector(random(width/2), random(height/2))
        
    def oscillate(self):
        self.angle.add(self.velocity)
        
    def display(self):
        x = sin(self.angle.x) * self.amplitude.x
        y = sin(self.angle.y) * self.amplitude.y
        
        ellipseMode(CENTER)
        
        pushMatrix()
    
        stroke(255)
        fill(255)
        translate(width/2, height/2)
        
        line(0, 0, x, y)
        ellipse(x, y, 20, 20)
        
        popMatrix()
        

def setup():
    size(640, 320)
    
    global oscillator
    oscillator = Oscillator()

def draw():
    background(0)
    oscillator.oscillate()
    oscillator.display()