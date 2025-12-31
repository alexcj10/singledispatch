"""
REAL WORLD PATTERN: Event Handling System
-----------------------------------------
Game engines and GUI frameworks often emit "Event" objects.
You need to handle each event differently.

Using `if isinstance(event, Click): ... elif ...` is slow and messy.
`singledispatch` acts as a perfect event router.
"""

from functools import singledispatch
from dataclasses import dataclass

# --- 1. The Events ---
@dataclass
class Event:
    pass

@dataclass
class PlayerMove(Event):
    x: int
    y: int

@dataclass
class PlayerAttack(Event):
    damage: int
    target: str

@dataclass
class GameQuit(Event):
    reason: str

# --- 2. The Event Router ---

@singledispatch
def handle_event(event):
    print(f"[Unhandled] Ignoring unknown event: {event}")

@handle_event.register(PlayerMove)
def _(e):
    print(f"MOVE: Player moved to ({e.x}, {e.y})")

@handle_event.register(PlayerAttack)
def _(e):
    print(f"ATTACK: Dealt {e.damage} damage to {e.target}!")

@handle_event.register(GameQuit)
def _(e):
    print(f"QUIT: Game over. Reason: {e.reason}")

# --- 3. The Game Loop Simulation ---

event_queue = [
    PlayerMove(x=10, y=20),
    PlayerAttack(damage=50, target="Orc"),
    "RandomGarbage",  # Simulating a bad event
    GameQuit(reason="Rage Quit")
]

print("--- Processing Event Queue ---")
for event in event_queue:
    handle_event(event)

