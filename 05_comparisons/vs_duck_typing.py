# DUCK TYPING
class Dog:
    def sound(self):
        print("Bark")

class Human:
    def sound(self):
        print("Hello")

def make_sound(obj):
    obj.sound()

make_sound(Dog())
make_sound(Human())

print("\n--- singledispatch ---\n")

from functools import singledispatch

@singledispatch
def make_sound(obj):
    print("Unknown sound")

@make_sound.register(Dog)
def _(obj):
    print("Bark")

@make_sound.register(Human)
def _(obj):
    print("Hello")

make_sound(Dog())
make_sound(Human())
