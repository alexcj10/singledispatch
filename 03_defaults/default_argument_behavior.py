from functools import singledispatchmethod

class Store:
    @singledispatchmethod
    def product(self, arg):
        """
        The registered function requires an argument to dispatch on.
        The wrapper does NOT look at default values to decide dispatch.
        """
        raise NotImplementedError("Default handler should not be reached if you always pass args")

    @product.register(str)
    def _(self, arg):
        print("STRING handler:", arg)

s = Store()

print("1. Call with argument (Works):")
s.product("Burger")  # Dispatches on "Burger" (str) -> STRING handler

print("\n2. Call without argument (Fails):")
try:
    s.product()
except TypeError as e:
    print(f"CRASHED as expected: {e}")

"""
LESSON:
`singledispatch` needs an ACTUAL value passed at runtime to determine the type.
It does NOT look at the default value defined in the function signature (e.g. `def product(self, arg="default")`)
to "guess" the type.

If you don't pass an argument, it has nothing to check the type of, so it crashes.
"""
