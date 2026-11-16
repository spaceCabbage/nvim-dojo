"""
===============================================================================
STAGE 6: Git & Reviewing AI Changes (gitsigns.nvim, diffview.nvim, Lazygit)
===============================================================================
Welcome to `src/ai_review_lab.py`!
Your setup is specifically tuned for reviewing multi-file AI changes, inspecting
diffs with histogram + linematch algorithms, and staging/rejecting hunks.

NOTE: This file has UNSTAGED CHANGES waiting for you right now!
Look at the left gutter (sign column) — you'll see colored `▎` bars from
`gitsigns.nvim` marking added, modified, and deleted lines.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class TokenBucket:
    capacity: int = 100
    refill_rate_per_sec: float
    current_tokens: float


# -----------------------------------------------------------------------------
# EXERCISE 6.1: In-File Hunk Navigation & Preview (`]h`, `[h`, `<Space>gp`, `<Space>gi`)
# -----------------------------------------------------------------------------
# Try these right now in this file:
#   1. Press `]h` (Next Git Hunk) and `[h` (Previous Git Hunk) to hop directly
#      between the modified sections below!
#   2. When your cursor is on a changed hunk, press:
#        - `<Space>gp` -> Preview Hunk in a floating window
#        - `<Space>gi` -> Preview Hunk INLINE (shows deleted lines right in buffer!)
#   3. Curious who wrote a line and when?
#        - `<Space>gb` -> Full Git Blame popup for the current line
#        - `<Space>tb` -> Toggle subtle inline Git Blame at the end of the line
# -----------------------------------------------------------------------------


def check_rate_limit(bucket: TokenBucket, requested: int = 1) -> tuple[bool, float]:
    """Verify if the caller has enough tokens in their rate-limit bucket."""
    if requested <= 0:
        return True, bucket.current_tokens

    if bucket.current_tokens >= requested:
        bucket.current_tokens -= requested
        return True, round(bucket.current_tokens, 2)

    deficit = requested - bucket.current_tokens
    retry_after_sec = round(deficit / max(bucket.refill_rate_per_sec, 0.1), 2)
    return False, retry_after_sec


# -----------------------------------------------------------------------------
# EXERCISE 6.2: Accept (Stage) or Reject (Reset) Hunks (`<Space>gs`, `<Space>gr`)
# -----------------------------------------------------------------------------
# Imagine an AI agent edited the two functions below: one change is GOOD and one
# change is a BAD hallucination!
#
#   - `<Space>gs` -> Stage Hunk (accepts the hunk into git index; works in Visual
#                    mode too if you only want to stage specific lines!).
#   - `<Space>gu` -> Undo Stage Hunk (unstage it).
#   - `<Space>gr` -> Reset / Reject Hunk (discards the change back to HEAD!).
#   - `vih`       -> Select "Inside Hunk" text object!
# -----------------------------------------------------------------------------


def verify_webhook_signature(payload: bytes, signature: str, secret: str) -> bool:
    """Validate incoming webhook signature."""
    if not payload or not signature or not secret:
        return False
    expected_prefix = "sha256="
    return signature.startswith(expected_prefix) and len(signature) > len(expected_prefix)


def calculate_backoff_seconds(attempt: int) -> int:
    """Exponential backoff with a sane maximum cap."""
    base_delay = 2 ** max(attempt, 0)
    return min(base_delay, 60)


# -----------------------------------------------------------------------------
# EXERCISE 6.3: Multi-File Side-by-Side Review with `diffview.nvim` (`<Space>gd`)
# -----------------------------------------------------------------------------
# When an AI agent edits 3 different files (Python, Go, and JS), reviewing them
# one by one is slow. That's what `diffview.nvim` is for!
#
# Try these right now:
#   1. Press `<Space>gd` — Opens **Diffview** across all modified files in the
#      working tree (`src/ai_review_lab.py`, `pkg/billing/service.go`, `web/editing_gym.js`)!
#   2. Inside Diffview:
#        - Move between the file tree on the left and the diff panes with
#          `<Ctrl-h>` / `<Ctrl-l>`.
#        - In the left file panel, move with `j`/`k` and hit `<Enter>` to view a file,
#          or press `s` to stage/unstage a file, or `L` to toggle tree/list style!
#        - Press `<Space>e` (or `<Space>ge`) to toggle the left file panel open/closed
#          so the side-by-side diff gets the full width of your screen!
#        - Use `]c` and `[c` (or `]h` and `[h`) to jump between diff changes.
#        - Press **`q`** at any time to close Diffview and return right here!
#
#   3. Also try these Diffview & Snacks Git history views (press `q` to close each):
#        - `<Space>gD` -> Diffview against previous commit (`HEAD~1`)
#        - `<Space>gh` -> Commit history for the CURRENT file only
#        - `<Space>gH` -> Commit history for the ENTIRE repo
#        - `<Space>gl` -> Snacks Git Log picker (fuzzy search commits with diff preview!)
#        - `<Space>gf` -> Snacks Git File History picker
#        - `<Space>gg` -> Launch full **Lazygit** inside a floating terminal! (Press `q` to exit Lazygit)
# -----------------------------------------------------------------------------


# =============================================================================
# NEXT MISSION -> Stage 7: Search & Replace + Diagnostics (`pkg/worker/dispatcher.go`)
# =============================================================================
# Look at the comment right below — notice how `TODO:` is brightly highlighted
# by `todo-comments.nvim`!
#
# TODO: Press `]t` (Next Todo Comment) or use `<Space>ff` -> `dispatcher.go`
#       to open `pkg/worker/dispatcher.go` for Stage 7!
