x = 100
y = 100

xspeed = 4
yspeed = 5

def setup():
    size(512, 256)
    background(0)
    
def draw():
    
    global x, y, xspeed, yspeed
    
    x += xspeed
    y += yspeed
    
    if x > width or x < 0:
        xspeed *= -1
        
    if y > height or y < 0:
        yspeed *= -1
        
    fill(255)
    ellipse(x, y, 10, 10)