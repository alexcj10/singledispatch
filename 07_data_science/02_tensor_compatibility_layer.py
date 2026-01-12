"""
02_tensor_compatibility_layer.py

Problem:
    AI Research often involves mixing codebases.
    - Model A is in PyTorch.
    - Model B is in TensorFlow.
    - Post-processing is in pure Numpy.
    
    You need utility functions (like `to_numpy` or `get_shape`) that work regardless of the framework.

Solution:
    `singledispatch` allows you to write a "Backend Agnostic" layer.
    You define the function once, and register adapters for each framework.
"""

from functools import singledispatch
import numpy as np
import torch
# import tensorflow as tf # Optional: Uncomment if TF is installed

@singledispatch
def to_numpy(tensor):
    """
    Converts any tensor-like object to a numpy array.
    """
    # Default fallback: Try to convert directly, works for lists/tuples
    try:
        return np.array(tensor)
    except Exception:
        raise TypeError(f"Object of type {type(tensor)} is not supported.")

@to_numpy.register(np.ndarray)
def _(tensor):
    # No-op if already numpy
    return tensor

@to_numpy.register(torch.Tensor)
def _(tensor):
    # PyTorch requires detaching gradients and moving to CPU first
    return tensor.detach().cpu().numpy()

# @to_numpy.register(tf.Tensor)
# def _(tensor):
#     # TensorFlow has a simple .numpy() method
#     return tensor.numpy()

def main():
    print("--- Framework Agnostic Tensor Operations ---\n")

    # 1. PyTorch Tensor (On CPU or GPU)
    pt_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
    print(f"Input: PyTorch Tensor (requires_grad={pt_tensor.requires_grad})")
    
    np_arr = to_numpy(pt_tensor)
    print(f"Output: Numpy Array\n{np_arr}\n")

    # 2. Pure Numpy Array
    orig_np = np.array([10, 20, 30])
    print(f"Input: Numpy Array")
    print(f"Output: {to_numpy(orig_np)}")

if __name__ == "__main__":
    main()
