"""
===============================================================================
STAGE 3: Teleporting Around Code (flash.nvim, Words, Buffers & Windows)
===============================================================================
Welcome to `src/navigation_teleport.py`!
In this file, you'll learn how to move anywhere on your screen in 2-3 keystrokes
without mashing `j`/`k`/`w`/`b`.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Waypoint:
    label: str
    sector: str
    coordinates: tuple[float, float, float]
    is_active: bool = True


# -----------------------------------------------------------------------------
# EXERCISE 3.1: Flash Jump (`s` in Normal, Visual, or Operator mode)
# -----------------------------------------------------------------------------
# How it works:
#   1. Press `s` (in Normal mode).
#   2. Type the first 1 or 2 characters of the word you want to jump to on screen
#      (for example, type `be` to target `beacon_omega` below, or `wa` for `warp_drive`).
#   3. Bright label letters appear next to every match on screen!
#   4. Press the single label letter to teleport your cursor directly there!
#
# Try jumping between these targets right now using `s`:
#   -> alpha_station        -> nebula_gate          -> quantum_relay
#   -> beacon_omega         -> warp_drive           -> hyper_thruster
# -----------------------------------------------------------------------------


def teleport_engine(
    origin: Waypoint,
    destination: Waypoint,
    fuel_reserve: float = 100.0,
) -> dict[str, object]:
    """Core navigation engine that calculates jump vectors between waypoints."""
    dx = destination.coordinates[0] - origin.coordinates[0]
    dy = destination.coordinates[1] - origin.coordinates[1]
    dz = destination.coordinates[2] - origin.coordinates[2]

    distance = (dx**2 + dy**2 + dz**2) ** 0.5
    fuel_cost = round(distance * 0.42, 2)
    remaining_fuel = fuel_reserve - fuel_cost

    if remaining_fuel < 0:
        return {
            "status": "ABORTED_INSUFFICIENT_FUEL",
            "distance": distance,
            "required_fuel": fuel_cost,
        }

    return {
        "status": "TELEPORT_LOCKED",
        "origin": origin.label,
        "destination": destination.label,
        "distance": round(distance, 3),
        "remaining_fuel": round(remaining_fuel, 2),
    }


# -----------------------------------------------------------------------------
# EXERCISE 3.2: Flash Treesitter Select (`S` in Normal or Visual mode)
# -----------------------------------------------------------------------------
# Want to select an entire function, `if` block, dictionary, or parameter list?
#   1. Put your cursor anywhere inside `teleport_engine` above.
#   2. Press `S` (capital S).
#   3. Flash highlights every syntax tree parent node with a single letter!
#   4. Press the letter for the dictionary, the `if` statement, or the whole
#      `def teleport_engine` function to visually select that exact block!
#   5. Press `<Esc>` to exit Visual mode.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# EXERCISE 3.3: Reference Jumping (`]]` and `[[`) via Snacks.words
# -----------------------------------------------------------------------------
# Put your cursor on the variable `distance` or `fuel_cost` inside `teleport_engine`:
#   - Notice how Neovim automatically underlines/highlights every use of that variable!
#   - Press `]]` to jump to the NEXT occurrence of that symbol.
#   - Press `[[` to jump to the PREVIOUS occurrence of that symbol.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# EXERCISE 3.4: Remote Flash (`r` after an operator like `y`, `d`, `c`)
# -----------------------------------------------------------------------------
# This feels like magic: you can yank, delete, or change text somewhere else on
# the screen AND your cursor automatically springs right back to where you started!
#
# Try it:
#   1. Keep your cursor right here on this comment.
#   2. Type `yr` (yank + remote), then type `qu` (to target `quantum_token_777` below),
#      press its Flash label letter, and then type `iw` (inner word).
#   3. You just copied `quantum_token_777` without moving your cursor! Press `p` to test.
#
#   Remote target ->   SECRET_KEY = "quantum_token_777"
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# EXERCISE 3.5: Buffers & Window Splits (`<Space>b...` and `<Space>w...`)
# -----------------------------------------------------------------------------
# You now have 3 buffers open (`README.md`, `02-finding-and-exploring.md`, and this file).
#
# Try Buffer Switching:
#   - `[b` and `]b`   -> Cycle to Previous / Next buffer
#   - `<Space>,`      -> Fuzzy pick from open buffers
#   - `<Space>bd`     -> Delete (close) current buffer cleanly without ruining window layout
#
# Try Window Splits & Navigation:
#   - `<Space>wv`     -> Split window Vertically
#   - `<Space>wh`     -> Split window Horizontally
#   - `<Ctrl-h/j/k/l>`-> Move between splits (AND seamlessly across Tmux panes!)
#   - `<Space>we`     -> Make split windows equal size
#   - `<Space>wc`     -> Close current window split
#   - `<Space>wo`     -> Close all OTHER splits ("only" keep current window)
# -----------------------------------------------------------------------------


# =============================================================================
# NEXT MISSION -> Stage 4: Editing Superpowers (`web/editing_gym.js`)
# =============================================================================
# Time to switch from Python to JavaScript!
# 1. Try opening a vertical split with `<Space>wv` (or stay in one window).
# 2. Press `<Space><Space>`, type `editing_gym`, and press `<Enter>` to open
#    `web/editing_gym.js`!
