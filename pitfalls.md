<h1 align="center">Common Pitfalls in singledispatch</h1>

### 1. Using `@singledispatch` on instance methods
**Problem**: `@singledispatch` dispatches on the *first* argument. For a method, the first argument is `self`. It will try to find a handler for `YourClass`, which is useless.
**Solution**: Use `@singledispatchmethod` (added in Python 3.8). It ignores `self` and dispatches on the second argument.
*See [02_methods/](./02_methods/)*

### 2. Expecting default arguments to trigger dispatch
**Problem**:
```python
@singledispatch
def func(arg="default"): ...

func() # CRASH!
```
**Reason**: Dispatch happens *at runtime based on the argument passed*. If you don't pass an argument, `singledispatch` has nothing to inspect.
**Solution**: Always pass an explicit argument, or handle `None` explicitly.
*See [03_defaults/](./03_defaults/)*

### 3. Registering the same type multiple times
**Problem**: The last registration wins silently.
**Solution**: Keep registrations organized. Don't split them across too many random files unless necessary.

### 4. Thinking `Union` works in Python < 3.7
**Problem**: Older Python versions didn't support `Union` inside `register`.
**Solution**: Use Python 3.7+. For Python 3.10+, you can use the `int | str` syntax.
*See [06_modern_typing/](./06_modern_typing/)*

### 5. Forgetting MRO (Method Resolution Order)
**Problem**: If you register `Sequence` and `list`, which one runs for a list?
**Answer**: `list` runs, because it is *more specific* than `Sequence`.
**Pitfall**: If you register `bool` and `int`, remember that **`bool` inherits from `int`** in Python!
```python
@func.register(int)
def _(x): print("INT")

func(True) # Prints "INT" unless you explicitly register bool!
```


