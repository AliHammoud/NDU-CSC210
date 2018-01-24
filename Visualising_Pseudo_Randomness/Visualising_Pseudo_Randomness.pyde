global random_counts
random_counts = range(20)

def setup():
    size(640, 240)
    
def draw():
    background(0)
    index = int(random(len(random_counts)))
    random_counts[index] += 1
    
    stroke(90)
    fill(255)
    
    w = width/len(random_counts)
    
    for x in range(len(random_counts)):
        rect(x * w, height - random_counts[x], w - 1, random_counts[x])