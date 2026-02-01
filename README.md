<h1 align="center">The Ultimate Guide to Python's <code>singledispatch</code> & <code>singledispatchmethod</code></h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue"/>
  <img src="https://img.shields.io/badge/license-MIT-green"/>
</p>

> **Stop writing `if isinstance(...)` chains forever.**  
> Master the cleanest, most extensible way to write polymorphic Python code.

---

## What is this?
This repository is a **comprehensive, zero-to-hero course** on `functools.singledispatch` and `singledispatchmethod`. 

It takes you from "I don't know what dispatch is" to "I can architect a plugin system using dispatch".

## Curriculum

### **Part 1: The Foundation**
- **[01_basics/](./01_basics/)**: The "Naive" way vs The "Pythonic" way.
- **[02_methods/](./02_methods/)**: How to use dispatch correctly inside Classes (hint: NOT `@singledispatch`).
- **[03_defaults/](./03_defaults/)**: Debugging the most common crash (Default Arguments).
- **[04_inheritance/](./04_inheritance/)**: How it handles subclassing automatically.
- **[05_comparisons/](./05_comparisons/)**: Why dispatch beats `if/else` chains and Duck Typing.

### **Part 2: Modern Mechanics (Python 3.10+)**
- **[06_modern_typing/unions.py](./06_modern_typing/unions.py)**: Dispatching on `int | float` (Union Types).
- **[06_modern_typing/collections_abc.py](./06_modern_typing/collections_abc.py)**: Dispatching on `Sequence`, `Mapping`, and other ABCs.
- **[06_modern_typing/protocols.py](./06_modern_typing/protocols.py)**: Dispatching on behavior (Duck Typing) using Protocols.

### **Part 3: Real World Patterns**
Don't just learn syntax. Build real systems.
- **[real_world/json_serializer.py](./real_world/json_serializer.py)**: Build a rock-solid JSON encoder for custom objects.
- **[real_world/event_handler.py](./real_world/event_handler.py)**: Build a cleanup game event router without massive `if/else` chains.

### **Part 3.5: Data Science & AI Patterns**
**NEW!** Learn why generic functions are cleaner than class-based polymorphism for ML pipelines.
- **[07_data_science/01_unified_preprocessing.py](./07_data_science/01_unified_preprocessing.py)**: Build a `clean_data()` pipeline that handles Lists, DataFrames, and Arrays.
- **[07_data_science/02_tensor_compatibility_layer.py](./07_data_science/02_tensor_compatibility_layer.py)**: Write backend-agnostic tensor ops (PyTorch/TF/Numpy).
- **[07_data_science/03_model_serialization.py](./07_data_science/03_model_serialization.py)**: A universal `save_model()` for Sklearn, PyTorch, and Keras.

### **Part 4: Deep Dive**
- **[deep_dive/how_dispatch_works.md](./deep_dive/how_dispatch_works.md)**: Visualizing the internal MRO cache and algorithm.
- **[deep_dive/performance.py](./deep_dive/performance.py)**: Is it slow? (Spoiler: No, but check the benchmarks).

---

## Quick Start

### The Problem
You have a function that needs to handle different types differently.

```python
# The Old Way: Hard to read, hard to extend
def process(data):
    if isinstance(data, str):
        print("Processing string")
    elif isinstance(data, list):
        print("Processing list")
    elif isinstance(data, int):
        print("Processing number")
```

### The Solution
```python
# The Singledispatch Way
from functools import singledispatch

@singledispatch
def process(data):
    print("Default handler (unknown type)")

@process.register(str)
def _(data):
    print("Processing string")

@process.register(list)
def _(data):
    print("Processing list")

@process.register(int)
def _(data):
    print("Processing number")
```

### Why is this better?
1.  **Open/Closed Principle**: You can add new types in a separate file/module without touching the original function.
2.  **Readability**: Each handler is a small, focused function.
3.  **Inheritance**: It automatically handles subclasses (e.g., if you register `Animal`, it works for `Dog` too).


### Dispatching for Class Methods
If you are working inside a class, use `@singledispatchmethod`. Standard `@singledispatch` will fail because it doesn't handle `self` correctly.

```python
from functools import singledispatchmethod

class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @singledispatchmethod
    def ctesting(self, value):
        print("Unsupported type:", type(value))

    @ctesting.register(str)
    def _(self, value):
        print("Name:", value, "| type:", type(value))

    @ctesting.register(int)
    def _(self, value):
        print("Age (int):", value, "| type:", type(value))

# 🔹 Object creation
obj = Test("alex", 2.0)

# 🔹 Method calls
obj.ctesting(obj.name)   # str → dispatched to str handler
obj.ctesting(obj.age)    # float → default handler
obj.ctesting(10)         # int → dispatched to int handler
```

---


## Common Pitfalls

Check out **[pitfalls.md](./pitfalls.md)** to avoid the top 5 mistakes developers make, such as:
1.  Using `@singledispatch` on methods (use `@singledispatchmethod`!).
2.  Expecting default arguments to trigger dispatch.
3.  Confusing `Union` types in older Python versions.

---

## Contributing
Found a new pattern? Open a PR! Let's make this the #1 resource for Python dispatching.

