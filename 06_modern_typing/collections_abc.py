"""
ABSTRACT BASE CLASSES (ABCs)
----------------------------
Instead of registering concrete types (like `list` or `dict`),
you can register Abstract Base Classes (ABCs).

This allows your code to work with ANY type that behaves like a list/dict,
even custom user classes!
"""

from functools import singledispatch
from collections.abc import Sequence, Mapping

@singledispatch
def processor(data):
    print("Unknown data type")

# This will match list, tuple, range, and custom sequence types
@processor.register(Sequence)
def _(data):
    # NOTE: We must exclude str because str is technically a Sequence too!
    if isinstance(data, (str, bytes)):
        print("Strings are special, not treating as sequence here.")
        return
    print(f"Processing sequence with {len(data)} items")

# This will match dict, functionality-like objects
@processor.register(Mapping)
def _(data):
    print(f"Processing mapping with keys: {list(data.keys())}")

processor([1, 2, 3])            # Sequence
processor({"a": 1, "b": 2})     # Mapping
processor((1, 2))               # Sequence

# Even broad types work!
processor(range(10))            # Sequence (range is a sequence!)
