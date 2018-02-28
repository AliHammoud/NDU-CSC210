global random_counts
random_counts = [0] * 20

def setup():
    size(640, 240)
    
def draw():
    background(0)
    
    index = int((len(random_counts) / 2) + ((len(random_counts) / 6) * randomGaussian()))
    print(index)
    
    if (index < len(random_counts) and random_counts[index] < height - 10):
        random_counts[index] += 1
    
    stroke(90)
    
    w = width/len(random_counts)
    
    for x in range(len(random_counts)):
        fill(random_counts[x])
        rect(x * w, height - random_counts[x], w, random_counts[x])