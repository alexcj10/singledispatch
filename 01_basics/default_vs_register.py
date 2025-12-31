from functools import singledispatch

@singledispatch
def process(x):
    print("DEFAULT: No matching type")

@process.register(str)
def _(x):
    print("STRING handler:", x)

print("Calling with string:")
process("Hello")   # str handler

print("\nCalling with int:")
process(100)       # default

"""
IMPORTANT RULE:
If a type is registered, default is ignored.
Default runs ONLY when no type matches.
"""
