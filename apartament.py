class Apartament:
    def __init__(self, number):
        self.number = number
        self.costs = {
            # cost_type - string: cost_ammount - int 
        }
    
    def __str__(self):
        return f"Apartamentul numarul {self.number}: {self.costs}"

    def getApartmentNumber(self):
        return self.number

    def addCost(self, type, cost):
        self.costs[type] = cost

    def deleteAllCosts(self):
        self.costs = {}

    def deleteCost(self, cost_type):
        if cost_type in self.costs:
            del self.costs[cost_type]
        else:
            raise KeyError()

    def totalCosts(self):
        total_sum = 0
        for cost in self.costs:
            total_sum += self.costs[cost]
        return total_sum

    def getCost(self, cost_type):
        return self.costs[cost_type]
