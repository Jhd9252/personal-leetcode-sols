from abc import ABC, abstractmethod

'''
1. Abstraction: Separate creation and implementation
2. Encapsulation: Entrap attributes and methods to be a black box , setting getters and setters and validation
3. Polymorphism: changing behavior (overriding, overloading)
4. inheritance: gain attributes and methods from parent 
'''


# 1. abstract class 
class Animal(ABC):

    # abstract method
    @abstractmethod
    def speak(self):
        pass 

# 4. inheritance 
class Canine(Animal):

    # 3. polymorphism: overriding
    # allowed in python
    def speak(self):
        print('Woof')

    # 3. polymorphism: overloading is not traditionally accepted in python
    # use *args, *kwargs, default values instead
    def speak(self, speech: str = None):
        if speech is None: 
            print('Woofing')
        else:
            print(speech)
        
# 4. concrete inheritance
class Dog(Canine):
    pass 
    # calling Canine methods still work because of inheritance


class BankAccount:
    def __init__(self, balance, pin):
        self._balance = balance
        self._pin = pin

    # @property makes an attribute read only
    @property
    def balance(self):
        return self._balance
    

    # @attribute.setter allows write access
    # onyl takes 2 args (self, newvalue)
    @balance.setter
    def balance(self, nv):
        self._balance = nv

    # if we want pin validation
    # then we need to create a custom method

if __name__ == '__main__':
    dog = Dog()
    dog.speak('hey there')
    dog.speak()
    dog.speak('uh oh')
    dog.speak()

    account = BankAccount(1000, 1234)
    print(account._balance) # calls balance() function
    # account.balance = 500 # Attribute Error because balance of BankAccount has no setter
    account.set_balance(1234) = -400