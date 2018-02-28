t = 0
x = 0

def setup():
    size (640, 100)
    background(0)
    
def draw():
    global t, x
    t += 0.01
    x += 0.1
    stroke(255)
    point(x, noise(t) * height)
    
    stroke (190, 190, 255, 150)
    point(x, random(1) * height)
    
    