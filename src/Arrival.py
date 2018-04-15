import math
import simpy as sim

class Arrival(object):

    def __init__(self, params):
        '''
        Constructor
        '''
        
    def generate(self):
        i=0
        while (self.sim.now() < G.maxTime):
        tnow = self.sim.now()
        arrivalrate =  100 + 10 * math.sin(math.pi * tnow/12.0)
        t = random.expovariate(arrivalrate)
        yield Sim.hold, self, t
        c = Car(name="Car%02d" % (i), sim=self.sim)
        timeParking = random.expovariate(1.0/G.parkingtime)
        self.sim.activate(c, c.visit(timeParking))
        i += 1