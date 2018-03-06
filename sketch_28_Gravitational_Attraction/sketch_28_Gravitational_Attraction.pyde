import Mover as m
import Attractor as a

def setup():
    size(512, 512)
    background(0)
    
    global mover, attractor, sim_speed
    mover = m.Mover()
    attractor = a.Attractor()
    
    #play with this value to see your visualization draw faster
    sim_speed = 1
    
def draw():
    
    for x in range(sim_speed):
        gravitational_pull = attractor.attract(mover)
        
        mover.add_force(gravitational_pull)
        mover.update()
        
        mover.display()
        attractor.display()
    