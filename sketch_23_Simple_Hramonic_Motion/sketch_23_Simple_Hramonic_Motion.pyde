amplitude = 250
period = 120

def setup():
    size(640, 320)

def draw():
    background(0)
    global amplitude, period
    
    x = amplitude * cos(TWO_PI * frameCount / period)
    
    fill(255)
    
    ellipseMode(CENTER)
    stroke(255)
    fill(255)
    translate(width/2, height/2)
    line(0, 0, x, 0)
    ellipse(x, 0, 20, 20)
    
    cycle_count = frameCount / period
    print('number of cycles: ' + str(cycle_count))