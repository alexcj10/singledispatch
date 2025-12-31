"""
REAL WORLD PATTERN: Custom JSON Serializer
------------------------------------------
The standard `json.dumps` fails when it encounters types it doesn't know (like sets, datetimes, or custom objects).
Using `singledispatch` is the CLEANEST way to build an extensible serializer.

Scenario:
You have a data pipeline containing mixed types:
- `datetime` objects
- `set` objects
- Custom `User` objects

Problem: `json.dumps` will crash.
Solution: Singledispatch!
"""

import json
from functools import singledispatch
from datetime import datetime
from dataclasses import dataclass

# --- 1. Our Data Models ---
@dataclass
class User:
    id: int
    name: str

# --- 2. The Serializer Logic ---

@singledispatch
def serialize(obj):
    """Fallback: If we don't know how to serialize it, convert to string."""
    return str(obj)

@serialize.register(datetime)
def _(obj):
    """Serialize datetime to ISO format."""
    return obj.isoformat()

@serialize.register(set)
def _(obj):
    """Sets aren't JSON compatible, so convert to sorted list."""
    return sorted(list(obj))

@serialize.register(User)
def _(obj):
    """Serialize our custom User object to a dict."""
    return {"__type__": "User", "id": obj.id, "name": obj.name}

# --- 3. Hooking it into json.dumps ---

def custom_json_encoder(obj):
    return serialize(obj)

# --- 4. Demo ---

data = {
    "timestamp": datetime.now(),
    "unique_ids": {1, 2, 3, 3, 2},  # set
    "user_info": User(id=42, name="Alice"),
    "simple_list": [10, 20]
}

print("Serializing complex data...")
# We use the 'default' argument of json.dumps to specify our dispatcher
json_str = json.dumps(data, default=custom_json_encoder, indent=2)

print(json_str)
