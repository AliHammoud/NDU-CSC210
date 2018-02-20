angle = 0
a_velocity = 0
a_acceleration = 0.001

def setup():
    size(512, 512)
    
def draw():
    
    background(0)
    
    global angle, a_velocity, a_acceleration
    
    stroke(255)
    fill (255)
    
    rectMode(CENTER)
    
    translate(width/2, height/2)

    rotate(angle)
    
    line(-50, 0, 50, 0)
    ellipse(50, 0, 8, 8)
    ellipse(-50, 0, 8, 8)
    
    a_velocity += a_acceleration
    
    print(a_velocity)
    
    if a_velocity < 0.25:
        angle += a_velocity
    else:
        angle += 0.25
    