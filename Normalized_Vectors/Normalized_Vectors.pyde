def setup():
    background(0)
    size(512, 512)
    
def draw():
    mouse = PVector(mouseX, mouseY)
    center = PVector(width/2, height/2)
    mouse.sub(center)
    
    mouse.normalize()
    
    mouse.mult(50)
    translate(width/2, height/2)
    
    stroke(255)
    line(0, 0, mouse.x, mouse.y)