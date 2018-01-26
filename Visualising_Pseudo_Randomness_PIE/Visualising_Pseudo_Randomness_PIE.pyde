#Idea by Fouad Sabeh

global diameters
diameters = [0] * 20


def setup():
    size(640, 360)

def draw():
    background(0)
    
    rand = int(random(len(diameters)))
    diameters[rand] += 1
    
    pieChart(diameters)


def pieChart(data):
    fill (255)
    stroke (0)
    for index in range(len(diameters)):
        arc(width/2 , height/2, data[index], data[index], (2*PI) / 20 * (index - 1), (2*PI) / 20 * index, PIE)