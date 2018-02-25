class CreatureA:
    def __init__(self):
        print('I am creature A')
        
class CreatureB:
    def __init__(self):
        print('I am creature B')
     
class Ecosystem:
    def __init__(self):
        print('An ecosystem has been created')
        #Use a dictionary to store/access creatures of similar species
        self.population = {}
    
    def spawn_creature_a(self):
        #Append the creature to its species list in the population dict
        return CreatureA()
    
    def spawn_creature_b(self):
        #Append the creature to its species list in the population dict
        return CreatureB()

#sample usage
eco = Ecosystem()

#let's spawn 20 of type CreatureA and 20 of type CreatureB
for x in range(20):
    eco.spawn_creature_a()
    eco.spawn_creature_b()