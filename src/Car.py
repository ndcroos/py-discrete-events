class Car(Sim.Process):
    
    def visit(self, timeParking=0):
        self.sim.parkedcars += 1
        self.sim.parking.observe(self.sim.parkedcars)
        yield Sim.hold, self, timeParking
        self.sim.parkedcars -= 1
        self.sim.parking.observe(self.sim.parkedcars)