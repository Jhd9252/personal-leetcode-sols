# Abstract base product
# concrete base product
# abstract decorator
# concrete decorators

from abc import ABC, abstractmethod

# abstract base 
class Coffee (ABC):
    def __init__(self):
        pass
    @abstractmethod
    def cost(self):
        pass 
    @abstractmethod
    def description(self):
        pass 

# concrete base
class Expresso(Coffee):
    def __init__(self):
        self._cost = 6
        self._description = 'Expresso'
    def cost(self):
        return self._cost
    def description(self):
        return self._description
    
# decorator abstract
# NOTE: Python dynamic binding allows this to "inherit" from coffee abstract
# NOTE: Python has multiple inheritance, so we can inhereit behavior from both
class ExtraDecorator(Coffee, ABC):
    @abstractmethod
    def __init__(selt, coffee: Coffee):
        self.coffee = coffee
    @abstractmethod
    def cost(self):
        pass 
    @abstractmethod
    def description(self):
        pass

class WhippedCream(ExtraDecorator):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
        self._cost = 2
        self._description = ' + whipped cream'

    def cost(self):
        return self.coffee.cost() + self._cost
    
    def description(self):
        return self.coffee.description() + self._description
    
class HazelNuts(ExtraDecorator):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
        self._cost = 1
        self._description = ' + hazelnut'

    def cost(self):
        return self.coffee.cost() + self._cost
    
    def description(self):
        return self.coffee.description() + self._description
    
if __name__ == "__main__":
    myexpresso = Expresso() # Express -> Coffee
    print('myexpresso is ', type(myexpresso))
    print(myexpresso.description(), myexpresso.cost())

    mywhippedexpresso = WhippedCream(myexpresso) # Whipped (Expresso (Coffee))
    print('expresso with whipped cream object is ', type(mywhippedexpresso))
    print(mywhippedexpresso.description(), mywhippedexpresso.cost())

    bwh = HazelNuts(mywhippedexpresso) # hazelnuts (whipped (expresso (Coffee)))
    print('expresso with whipped cream with hazelnut', type(bwh))
    print(bwh.description(), bwh.cost())






    




