xoff = 0
yoff = 0
offset = 0

def setup():
    background(0)
    size(512, 256)
    
def draw():
    global xoff, yoff, offset
    
    loadPixels()
    for x in range(width/2):
        for y in range(height):
            pixels[x + y * width] = color(random(255))
    
    for x in range(width/2):
        yoff = 0
        for y in range(height):
            pixels[x + y * width + width/2] = color(map(noise(xoff, yoff), 0, 1, 0, 255))
            yoff += 0.01
        xoff += 0.01
    updatePixels()
    offset += 1
    
            