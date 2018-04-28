def branch(angle, _length, sw):
    line (0, 0, 0, - _length)
    translate(0, -_length)
    
    pushMatrix()
    rotate(radians(angle))
    if _length > 10:
        branch(angle * 1.25, _length * 0.7, sw * 0.75)
    popMatrix()
    
    pushMatrix()
    rotate(-radians(angle))
    if _length > 10:
        branch(angle * 1.25, _length * 0.7, sw * 0.75)
    popMatrix()
    
def setup():
    size(512, 512)
    stroke(255)
   
global _angle
_angle = 0

def draw():
    
    background(0)
    translate(width/2, height)
    
    global _angle
    if _angle < 45:
        _angle += 0.1
    
    branch(_angle, height/4, 5)