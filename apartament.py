from datetime import date

class Apartament:
    def __init__(self, number):
        self.number = number
        self.costs = {
            # cost_type - string: cost_ammount - int 
        }
        self.costs_dates = {
            # cost_type - string: cost_date - date
        }
    
    def __str__(self):
        return f"Apartamentul numarul {self.number}: {self.costs}"

    def getApartmentNumber(self):
        return self.number

    def addCost(self, cost_type, cost):
        if cost_type in self.costs:
            input(f"Exista deja o cheltuiala la {cost_type}")
            return
        self.costs[cost_type] = cost
        self.costs_dates[cost_type] = date.today()

    def modifyCost(self, cost_type, cost):
        if cost_type in self.costs:
            self.costs[cost_type] = cost
            self.costs_dates[cost_type] = date.today()
        else:
            input(f"Nu exista cheltuieli la {cost_type}")

    def deleteAllCosts(self):
        self.costs = {}
        self.costs_dates = {}

    def deleteCost(self, cost_type):
        if cost_type in self.costs:
            del self.costs[cost_type]
            del self.costs_dates[cost_type]
        else:
            raise KeyError()

    def totalCosts(self):
        total_sum = 0
        for cost in self.costs:
            total_sum += self.getCost(cost)
        return total_sum

    def getCost(self, cost_type):
        try:
            return self.costs[cost_type]
        except KeyError:
            return 0
    
    def copy(self):
        new_apartment = Apartament(self.number)
        new_apartment.costs = dict(self.costs)
        new_apartment.costs_dates = dict(self.costs_dates)
        return new_apartment

    def getDate(self, cost_type):
        try:
            return self.costs_dates[cost_type]
        except KeyError:
            return date(1, 1, 1)