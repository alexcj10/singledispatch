"""
MODERN TYPING: Unions (Python 3.10+)
------------------------------------
You can register multiple types at once using the `|` operator (or `Union`).
This effectively allows "multiple alias" handlers.

Requirement: Python 3.10+ (for `|` syntax)
"""

from functools import singledispatch

@singledispatch
def formatter(x):
    print("Default:", x)

# 1. Registering multiple types with `|`
# This function handles BOTH int AND float
@formatter.register(int | float)
def _(x):
    print(f"Number: {x:.2f}")

# 2. Registering multiple types with `Union` (older style)
from typing import Union
@formatter.register(Union[list, tuple])
def _(x):
    print(f"Sequence of length {len(x)}")

# 3. Handling None (Optional)
@formatter.register(type(None))
def _(x):
    print("Received nothing!")

formatter(10)       # Number: 10.00
formatter(3.14)     # Number: 3.14
formatter([1, 2])   # Sequence of length 2
formatter((1, 2))   # Sequence of length 2
formatter(None)     # Received nothing!
