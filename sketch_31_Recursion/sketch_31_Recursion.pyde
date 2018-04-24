def setup():
    size(1024, 1024)
    background(0)
    stroke(255)
    noFill()
    
    draw_circles(780)
    #draw_circles_two(width/2, 780)
    #draw_circles_four(width/2, height/2, 780)
    
#One recursion
def draw_circles(radius):
    ellipse(width/2, height/2, radius, radius)
    
    if radius > 10:
        draw_circles(radius * 0.75)

#Two recursions
def draw_circles_two(x, radius):
    ellipse(x, height/2, radius, radius)
    
    if radius > 10:
        draw_circles_two(x + radius/2, radius/2)
        draw_circles_two(x - radius/2, radius/2)

#Four recursions
def draw_circles_four(x, y, radius):
    ellipse(x, y, radius, radius)
    
    if radius > 10:
        draw_circles_four(x + radius/2, y, radius/2)
        draw_circles_four(x - radius/2, y, radius/2)
        draw_circles_four(x, y + radius/2, radius/2)
        draw_circles_four(x, y - radius/2, radius/2)


def draw():
    pass
    