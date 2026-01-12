"""
01_unified_preprocessing.py

Problem:
    In Data Science pipelines, your data often changes formats. 
    - Early experimentation: Python Lists
    - Data Loading: Pandas DataFrames
    - Feature Engineering: Numpy Arrays

    Writing a `clean_data(data)` function usually leads to a mess of `if isinstance(data, pd.DataFrame): ...`.

Solution:
    Use `singledispatch` to create a unified API `clean_data()` that handles each type with specialized logic.
    This keeps your code cleaner and allows you to add support for new types (like Polars or Dask) 
    in separate files without breaking existing code.
"""

from functools import singledispatch
from typing import List, Union
import numpy as np
import pandas as pd

# 1. Define the interface
@singledispatch
def clean_data(data) -> Union[pd.DataFrame, np.ndarray, List]:
    """
    Cleans data by filling missing values with 0.
    Default behavior: Error out for unknown types.
    """
    raise NotImplementedError(f"Cannot clean data of type {type(data)}")

# 2. Register handler for Pandas DataFrames
@clean_data.register(pd.DataFrame)
def _(data: pd.DataFrame) -> pd.DataFrame:
    print(f"Dataset Shape: {data.shape} | Type: DataFrame")
    # Pandas specific logic
    return data.fillna(0)

# 3. Register handler for Numpy Arrays
@clean_data.register(np.ndarray)
def _(data: np.ndarray) -> np.ndarray:
    print(f"Dataset Shape: {data.shape} | Type: Numpy Array")
    # Numpy specific logic
    return np.nan_to_num(data, nan=0.0)

# 4. Register handler for Python Lists
@clean_data.register(list)
def _(data: list) -> list:
    print(f"Dataset Length: {len(data)} | Type: List")
    # List specific logic
    return [x if x is not None else 0 for x in data]

def main():
    print("--- Unified Data Cleaning Pipeline ---\n")

    # Scenario 1: Raw data from API (List with Nones)
    raw_list = [1.5, None, 2.3, None, 5.0]
    cleaned_list = clean_data(raw_list)
    print(f"Result: {cleaned_list}\n")

    # Scenario 2: Data loaded for analysis (Pandas with NaNs)
    df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
    cleaned_df = clean_data(df)
    print(f"Result:\n{cleaned_df}\n")

    # Scenario 3: Feature matrix for ML (Numpy with NaNs)
    arr = np.array([[1.0, np.nan], [np.nan, 4.0]])
    cleaned_arr = clean_data(arr)
    print(f"Result:\n{cleaned_arr}")

if __name__ == "__main__":
    main()
