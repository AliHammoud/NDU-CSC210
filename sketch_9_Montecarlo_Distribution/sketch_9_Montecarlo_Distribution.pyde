def montecarlo():
    while(True):
        r1 = random(1)
        probability = r1
        r2 = random(1)
        
        if(r2 < pow(probability, 5)):
            return r1

def setup():
    size(512, 512)
    background(0)

def draw():
    
    noStroke()
    fill(255,255,255,10)
    
    rect (width/2 - 150, 0 + montecarlo() * height, 100, 20)
    rect (width/2 + 50, 0 + random(1) * height, 100, 20)
    
    
    
    
    