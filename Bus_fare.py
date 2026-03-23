class vehicle():
    def __init__(self,time,cost_per_hour):
        self.time=time
        self.cost_per_hour=cost_per_hour
        print("the amount of money needed to pay for the fare is",self.time*self.cost_per_hour)
class bus(vehicle):
    def __init__(self, time, cost_per_hour):
        super().__init__(time, cost_per_hour)
obj= bus(3,3)
