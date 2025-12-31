"""
NORMAL FUNCTION vs SINGLEDISPATCH
--------------------------------
Problem:
One function, different behaviors based on input type.
"""

# ❌ WITHOUT singledispatch (The "Naive" Way)
# Problem: You have to write a giant if/elif/else chain.
# As you add support for more types, this function grows forever.
def describe_value(x):
    if isinstance(x, int):
        print("This is an integer:", x)
    elif isinstance(x, str):
        print("This is a string:", x)
    elif isinstance(x, list):
        print("This is a list:", x)
    else:
        print("Unknown type")

describe_value(10)
describe_value("Milk")
describe_value([1, 2, 3])

print("\n--- Using singledispatch ---\n")

# ✅ WITH singledispatch (The "Pythonic" Way)
# Solution: Separate the logic for each type into its own function.
# This makes the code extensible: other users can adding support for new types
# without modifying your original code!
from functools import singledispatch

@singledispatch
def describe_value(x):
    """
    This is the DEFAULT function.
    It runs ONLY if no registered type matches the input.
    """
    print("Default handler: Unknown type")

@describe_value.register(int)
def _(x):
    print("Integer handler:", x)

@describe_value.register(str)
def _(x):
    print("String handler:", x)

@describe_value.register(list)
def _(x):
    print("List handler:", x)

describe_value(10)
describe_value("Milk")
describe_value([1, 2, 3])
describe_value(3.14)  # Falls back to default handler
