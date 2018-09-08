x = 1
y = 1
iter = 0.001

def setup():
    size(512, 512)
    background(0)
    stroke(255)
    
def draw():
    global x, y, iter
    if(x <= 1):
        x -= iter
        y -= iter
        point(x * width, height - pow(x, y) * height)