# How `singledispatch` Works Under the Hood

When you decorate a function with `@singledispatch`, you aren't just getting a simple dictionary lookup. You are getting a robust, cached **Method Resolution Order (MRO) aware** dispatcher.

## 1. The Dispatch Algorithm

When you call `func(arg)`, `singledispatch` performs the following steps:

1.  **Check the Cache**: It checks a specialized internal cache to see if the type of `arg` has been seen before.
    -   *If yes*: Jump directly to the handler (O(1) speed).
2.  **Calculate Implementation**: If not in cache, it calculates which handler to use.
    -   It looks at the **MRO** (inheritance chain) of the argument's class.
    -   It finds the *closest* registered type in that chain.
    -   Example: If you pass a `Bool`, and `Bool` isn't registered, it checks `Int`. If `Int` is registered, it uses that. If not, it checks `Object`.
3.  **Update Cache**: The result is stored so the next time you pass this same type, it's instant.

## 2. Why is this better than a Dict Lookup?

A simple dictionary `{type: func}` fails with inheritance.

```python
# Naive approach
handlers = {Animal: handle_animal}

def dispatch(x):
    return handlers.get(type(x))

# Problem:
class Dog(Animal): pass
dispatch(Dog())  # Returns None! Dog is not explicitly in the dict.
```

`singledispatch` solves this by walking the MRO. `Dog` inherits from `Animal`, so `singledispatch` correctly matches it to `Animal`.

## 3. The `_find_impl` Method

Internally, specific versions of Python use a C-accelerated version or a pure Python fallback. The logic resembles:

```python
def _find_impl(cls, registry):
    for base in cls.__mro__:
        if base in registry:
            return registry[base]
    return registry[object]
```

## 4. Performance Implications

-   **Cold Start**: The first time you pass a new type, there is a small cost to walk the MRO.
-   **Warm**: Subsequent calls are as fast as a dictionary lookup (key=class, value=function).
-   **Cache Busting**: The cache is robust and doesn't leak memory for new dynamic types in most standard implementations.

## 5. View the Registry

You can actually inspect the registry!

```python
@singledispatch
def func(x): ...

print(func.registry.keys())
# Output: dict_keys([<class 'object'>, <class 'int'>, ...])
```
