"""
PROTOCOLS (Structural Subtyping)
--------------------------------
Protocols allow you to dispatch on objects that HAVE a certain method,
regardless of what class they inherit from.

NOTE: `singledispatch` does NOT support Protocols directly out of the box in standard runtime
because `isinstance(x, Protocol)` checks are tricky. 
However, for educational purposes, if you use a runtime-checkable protocol, it DOES work!
"""

from functools import singledispatch
from typing import Protocol, runtime_checkable

# 1. Define a Protocol
@runtime_checkable
class Quacks(Protocol):
    def quack(self) -> None:
        ...

# 2. Define classes that implement it implicitly (no inheritance!)
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm imitating a duck... Quack!")

class Dog:
    def bark(self):
        print("Woof!")

# 3. Setup Dispatch
@singledispatch
def make_noise(x):
    print("Unknown noise maker")

@make_noise.register(Quacks)
def _(x):
    print("It quacks! Let's make it quack:")
    x.quack()

# 4. Test it
d = Duck()
p = Person()
dog = Dog()

print("--- Duck ---")
make_noise(d)   # Works!

print("\n--- Person ---")
make_noise(p)   # Works! (even though Person does not inherit from Quacks)

print("\n--- Dog ---")
make_noise(dog) # Unknown noise maker (Dog doesn't have .quack())
