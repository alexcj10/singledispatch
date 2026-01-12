"""
03_model_serialization.py

Problem:
    Saving models requires different strategies.
    - Scikit-Learn: Use `joblib` or `pickle`.
    - PyTorch: Use `torch.save(model.state_dict(), ...)`
    - TensorFlow/Keras: Use `model.save(...)`
    - HuggingFace: Use `model.save_pretrained(...)`

    A generic `save_model(model, path)` usually becomes a nightmare of imports and if-checks.

Solution:
    Use `singledispatch` to route the save call to the correct library.
"""

from functools import singledispatch
import os
import joblib
from sklearn.base import BaseEstimator
from sklearn.linear_model import LinearRegression
import torch
import torch.nn as nn

# 1. The Generic API
@singledispatch
def save_artifact(model, path: str):
    """
    Saves a machine learning artifact to disk.
    """
    raise NotImplementedError(f"Don't know how to save model of type {type(model)}")

# 2. Scikit-Learn Handler
# Matches ANY class that inherits from BaseEstimator
@save_artifact.register(BaseEstimator)
def _(model, path: str):
    print(f"📦 Saving Scikit-Learn model to {path} using joblib...")
    joblib.dump(model, path)
    print("Done.")

# 3. PyTorch Handler
# Matches ANY class that inherits from torch.nn.Module
@save_artifact.register(nn.Module)
def _(model, path: str):
    print(f"🔥 Saving PyTorch model weights to {path} using torch.save...")
    torch.save(model.state_dict(), path)
    print("Done.")

def main():
    print("--- Universal Model Serializer ---\n")
    
    # Example 1: Saving a generic Sklearn Model
    sklearn_model = LinearRegression()
    sklearn_model.fit([[0, 0], [1, 1]], [0, 1])
    save_artifact(sklearn_model, "temp_sklearn_model.pkl")
    print("\n")

    # Example 2: Saving a Deep Learning Model
    torch_model = nn.Linear(10, 1)
    save_artifact(torch_model, "temp_torch_weights.pth")

    # Cleanup
    if os.path.exists("temp_sklearn_model.pkl"):
        os.remove("temp_sklearn_model.pkl")
    if os.path.exists("temp_torch_weights.pth"):
        os.remove("temp_torch_weights.pth")

if __name__ == "__main__":
    main()
