# Director (Head Chef)
# Abstract Builder (Cook guidelines)
# Concrete Cooks (actual cooks)
# product

from abc import ABC, abstractmethod

# Product class
class Pizza:
    def __init__(self):
        self.crust = None
        self.cheese = None
        self.sauce = None
        self.toppings = []

    def __str__(self):
        return f'{self.crust}, {self.cheese}, {self.sauce}, {self.toppings}'

# abstract builder (recipe)
class PizzaBuilder(ABC):
    @abstractmethod
    def __init__(self): pass 
    @abstractmethod
    def set_crust(self): pass
    @abstractmethod
    def set_cheese(self): pass
    @abstractmethod
    def set_sauce(self): pass 
    @abstractmethod
    def set_toppings(self): pass
    @abstractmethod
    def get_pizza(self): pass

# concrete 
class MexicanPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    def set_crust(self):
        self.pizza.crust = 'thin'
    def set_cheese(self):
        self.pizza.cheese = 'light'
    def set_sauce(self):
        self.pizza.sauce = 'marinara'
    def set_toppings(self):
        self.pizza.toppings = ['everything meximcan']
    def get_pizza(self): 
        return self.pizza

# DIRECTOR(head chef)
class PizzaDirector:
    
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def build_pizza(self):
        self.builder.set_crust()
        self.builder.set_cheese()
        self.builder.set_sauce()
        self.builder.set_toppings()
        return self.builder.get_pizza()
    
if __name__ == '__main__':
    builder = MexicanPizzaBuilder()
    director = PizzaDirector(builder)
    pizza = director.build_pizza()
    print(pizza)
