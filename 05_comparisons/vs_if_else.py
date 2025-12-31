# ❌ if-else version
def handle(x):
    if isinstance(x, int):
        print("INT:", x)
    elif isinstance(x, str):
        print("STR:", x)
    elif isinstance(x, list):
        print("LIST:", x)
    else:
        print("OTHER")

handle(10)
handle("Milk")
handle([1, 2])

print("\n--- singledispatch version ---\n")

from functools import singledispatch

@singledispatch
def handle(x):
    print("OTHER")

@handle.register(int)
def _(x):
    print("INT:", x)

@handle.register(str)
def _(x):
    print("STR:", x)

@handle.register(list)
def _(x):
    print("LIST:", x)

handle(10)
handle("Milk")
handle([1, 2])
