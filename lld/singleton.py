# Singleton is builder pattern
# Emphasizes a single object creation 
# With a single entry point

class Singleton:

    # in python convention, _attribute is a private attribute
    # in python convention, attributes outside class methods are static -> shared 

    # this creates a static (shared), private variable
    _instance = None

    # __new__ is similar to __init__
    # __new__ is called before __init__
    # __new__ is for class creation, while __init__ is for instance instantiation

    def __new__(cls):
        
        # we check the shared private and static variable
        if cls._instance is None:

            # if it single entry not created, call upon super().__new__(cls) to create it
            # since we are overriding the __new__ method of this class, we can instantiate it
            # using Object.__new__(cls) allows us to super python's origin Object class to create this Singleton
            cls._instance = super().__new__(cls)

        # only return the single shared created class with single entry point 
        return cls._instance
    

if __name__ == '__main__':

    instance1 = Singleton()
    instance2 = Singleton()
    
    print(instance1 == instance2)
    print(instance1 is instance2)