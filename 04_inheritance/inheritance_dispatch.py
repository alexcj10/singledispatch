from functools import singledispatch

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

@singledispatch
def speak(x):
    print("Unknown creature")

@speak.register(Animal)
def _(x):
    print("Animal sound")

print("Dog speaks:")
speak(Dog())

print("Cat speaks:")
speak(Cat())

"""
Why this works:
Python checks MRO (Method Resolution Order)

Dog → Animal → object

Closest registered parent wins.
"""
