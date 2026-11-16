"""
===============================================================================
STAGE 5: Code Intelligence, Autocomplete & Formatting (LSP, blink.cmp, conform)
===============================================================================
You jumped here via `gd` (Go to Definition)!
Tip: Press `<Ctrl-o>` at any time to jump BACK to your previous cursor location
in the jump list, and `<Ctrl-i>` to jump FORWARD again!
"""

from typing import Iterable
from src.models.invoice import InvoiceItem


# -----------------------------------------------------------------------------
# EXERCISE 5.1: LSP Navigation & Hover (`gd`, `gr`, `K`, `<Space>cs`, `<Space>th`)
# -----------------------------------------------------------------------------
# Try these right now on `InvoiceItem` or `calculate_invoice_total` below:
#   - `K`          -> Hover Documentation popup (press `K` a second time to jump
#                     inside the floating doc window to scroll, then `q` to close!).
#   - `gd`         -> Go to Definition (try pressing `gd` on `InvoiceItem` above,
#                     then press `<Ctrl-o>` to come right back here!).
#   - `gr`         -> Find All References in Snacks Picker (try `gr` on
#                     `calculate_invoice_total`—it shows both this file and
#                     `src/editing_gym.py`!).
#   - `<Space>cs`  -> Document Symbols / Outline (lists every class, function, and
#                     variable in this file so you can fuzzy-jump to any method!).
#   - `<Space>cS`  -> Workspace Symbols across the whole project.
#   - `<Space>th`  -> Toggle LSP Inlay Hints on/off.
# -----------------------------------------------------------------------------


def calculate_invoice_total(items: Iterable[InvoiceItem], tax_rate: float = 0.0) -> dict[str, int]:
    """Calculate subtotal, tax, and grand total (in cents) for a list of invoice items."""
    subtotal = sum(item.subtotal_cents for item in items)
    tax_cents = round(subtotal * tax_rate)
    grand_total = subtotal + tax_cents
    return {
        "subtotal_cents": subtotal,
        "tax_cents": tax_cents,
        "grand_total_cents": grand_total,
    }


class InvoiceService:
    """Service responsible for validating, pricing, and summarizing customer invoices."""

    def __init__(self, tax_rate: float = 0.0825, currency: str = "USD") -> None:
        self.tax_rate = tax_rate
        self.currency = currency

    def summarize(self, customer_name: str, items: list[InvoiceItem]) -> str:
        totals = calculate_invoice_total(items, self.tax_rate)
        dollars = totals["grand_total_cents"] / 100.0
        return f"Invoice for {customer_name}: {dollars:.2f} {self.currency}"


# -----------------------------------------------------------------------------
# EXERCISE 5.2: Project-Wide Symbol Rename (`<Space>cr`) & Code Actions (`<Space>ca`)
# -----------------------------------------------------------------------------
# 1. Put your cursor on `format_currency_label` below.
# 2. Press `<Space>cr` (Code Rename).
# 3. A sleek input box pops up! Type a new name (like `render_currency_badge`) and
#    hit `<Enter>` — notice how every call to it updates automatically!
# -----------------------------------------------------------------------------
def format_currency_label(amount_cents: int, symbol: str = "$") -> str:
    return f"{symbol}{amount_cents / 100:.2f}"


def preview_receipt() -> str:
    return format_currency_label(12500)


# -----------------------------------------------------------------------------
# EXERCISE 5.3: Blazing Autocomplete (`blink.cmp` + `nvim-autopairs`)
# -----------------------------------------------------------------------------
# Inside `test_autocomplete` below, open a new line in Insert mode (`o`) and type:
#   `item.`
# Watch `blink.cmp` pop up instant completions from Pyright (`description`,
# `discount_percent`, `quantity`, `sku`, `subtotal_cents`, `unit_price_cents`)!
#   - `<C-n>` / `<C-p>` -> Select next / previous item
#   - `<Tab>` or `<CR>` -> Accept completion
#   - `<C-Space>`       -> Manually summon completion or toggle documentation window
#   - `<C-f>` / `<C-b>` -> Scroll documentation popup down / up
# -----------------------------------------------------------------------------
def test_autocomplete(item: InvoiceItem) -> int:
    # Put cursor here, press `o`, and type `return item.`
    return item.subtotal_cents


# -----------------------------------------------------------------------------
# EXERCISE 5.4: Auto-Formatting with `conform.nvim` (`<Space>cf` & `<Ctrl-s>`)
# -----------------------------------------------------------------------------
# Look how ugly `messy_unformatted_calc` below is!
#   1. Press `<Space>cf` (Code Format) OR simply save the file with `<Ctrl-s>`!
#   2. `conform.nvim` runs `ruff` automatically and formats the whole file cleanly!
#   3. Need to edit a file WITHOUT triggering format-on-save? Press `<Space>tf`
#      (Toggle Format on Save) to turn auto-formatting off or back on!
# -----------------------------------------------------------------------------
def messy_unformatted_calc(  x:int,y:   int,   z:int=10 )->dict[str,int]:
    result=x+y*z
    return {"x":x,"y":y,"z":z,"result":   result}


# =============================================================================
# NEXT MISSION -> Stage 6: Git & Reviewing AI Changes (`src/ai_review_lab.py`)
# =============================================================================
# I've left some unstaged "AI-generated" edits in this repository for you to review!
#
# Jump to Stage 6 using the **Git Status Picker**:
#   1. Press `<Space>gst` (Git Status Files).
#   2. Notice how `src/ai_review_lab.py` has a live diff preview right inside the picker!
#   3. Select `src/ai_review_lab.py` and press `<Enter>`.
