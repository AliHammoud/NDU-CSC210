import copy

size(640, 360)
noLoop()
background(255)

# Establish a range of values on the complex plane
# A different range will allow us to "zoom" in or out on the fractal

# It all starts with the width, try higher or lower values
w = 4
h = (w * height) / width

# Start at negative half the width and height
xmin = -w/2
ymin = -h/2

# Make sure we can write to the pixels[] array.
# Only need to do this once since we don't do any other drawing.
loadPixels()
# Maximum number of iterations for each poon the complex plane
maxiterations = 100

# x goes from xmin to xmax
xmax = xmin + w
# y goes from ymin to ymax
ymax = ymin + h

# Calculate amount we increment x,y for each pixel
dx = (xmax - xmin) / (width)
dy = (ymax - ymin) / (height)

# Start y
y = ymin
for j in range(height):
    # Start x
    x = xmin
    for i in range(width):
        # Now we test, as we iterate z = z^2 + cm does z tend towards infinity?
        a = copy.deepcopy(x)
        b = copy.deepcopy(y)
        n = 0
        while n < maxiterations:
            #print('########', a)
            aa = a * a
            bb = b * b
            twoab = 2.0 * a * b
            a = aa - bb + x
            b = twoab + y
            #print('---------', a)
            # Infinty in our finite world is simple, let's just consider it 16
            #print(dist(aa, bb, 0, 0))
            if (dist(aa, bb, 0, 0) > 4.0):
                break    # Bail
            
            n += 1
                

        # We color each pixel based on how long it takes to get to infinity
        # If we never got there, let's pick the color black
        if (n == maxiterations):
            pixels[i+j*width] = color(0)
        else:
            # Gosh, we could make fancy colors here if we wanted
            _norm = map(n, 0, maxiterations, 0, 1)
            pixels[i+j*width] = color(map(sqrt(_norm), 0, 1, 0, 255))
        
        x += dx

    y += dy

updatePixels()
print('done')