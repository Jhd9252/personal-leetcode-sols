# Abstract base product
# concrete base product
# abstract decorator
# concrete decorators

'''
Decorator Pattern
(1) Abstract base product
(2) concrete base product
(3) Abstract decorator
(4) concrete decorators
'''

from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def __init__(self):
        pass 
    @abstractmethod
    def cost(self):
        pass
    @abstractmethod
    def desc(self):
        pass

class Expresso(Coffee):
    def __init__(self):
        self._cost = 5
        self._desc = 'Expresso '

    def cost(self):
        return self._cost

    def desc(self):
        return self._desc
    
# decorator abstract
# NOTE: Python dynamic binding allows this to "inherit" from coffee abstract
# NOTE: Python has multiple inheritance, so we can inhereit behavior from both
# Construct with a coffee object, so there is no need for inheritance really in the first place 

class ExtraDecorator(ABC):
    @abstractmethod
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
    @abstractmethod
    def cost(self):
        pass
    @abstractmethod
    def desc(self):
        pass 


class WhippedCream(ExtraDecorator):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
        self._cost = 2
        self._desc = '+ whipped cream'

    def cost(self):
        return self.coffee.cost() + self._cost 
    
    def desc(self):
        return self.coffee.desc() + self._desc
    
class HazelNuts(ExtraDecorator):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee
        self._cost = 1
        self._desc = '+ hazelnuts'
    def cost(self):
        return self.coffee.cost() + self._cost
    
    def desc(self):
        return self.coffee.desc() + self._desc
    
if __name__ == "__main__":
    expresso = Expresso()
    print(expresso.desc() + ': ' + str(expresso.cost()))

    whippedexpresso = WhippedCream(expresso)
    print(whippedexpresso.desc() + ': ' + str(whippedexpresso.cost()))
    print(type(whippedexpresso))
    hazelnuts = HazelNuts(whippedexpresso)
    print(hazelnuts.desc() + ': ' + str(hazelnuts.cost()))







    




