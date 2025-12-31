"""
WRONG WAY:
Using @singledispatch on instance methods
"""

from functools import singledispatch

class Store:
    @singledispatch
    def product(self, item):
        print("DEFAULT product")

    @product.register(str)
    def _(self, item):
        print("STRING product")

s = Store()
s.product("Milk")

"""
Why this is WRONG:
- singledispatch checks FIRST argument
- Here first argument is `self`
- type(self) is always Store
So str handler NEVER runs
"""
