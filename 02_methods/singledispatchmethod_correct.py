"""
CORRECT WAY: singledispatchmethod
---------------------------------
For classes, you CANNOT use `singledispatch`. 
Why? Because the first argument to a method is `self`.
`singledispatch` would try to dispatch on `self` (the instance), which is useless.

`singledispatchmethod` handles this by ignoring `self` and dispatching on the *second* argument.
"""

from functools import singledispatchmethod

class Store:
    @singledispatchmethod
    def product(self, item):
        print("DEFAULT product:", item)

    @product.register(str)
    def _(self, item):
        print("STRING product:", item)

    @product.register(list)
    def _(self, item):
        print("LIST of products:", item)

s = Store()

s.product("Milk")
s.product(["Milk", "Bread"])
s.product(100)

"""
IMPORTANT:
singledispatchmethod ignores `self`
and dispatches on `item`
"""
