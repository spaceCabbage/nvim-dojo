"""Data models for invoices (used by Stage 5 LSP exercises)."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class InvoiceItem:
    """Represents a single billable line item on a customer invoice."""

    sku: str
    description: str
    quantity: int
    unit_price_cents: int
    discount_percent: float = 0.0
    notes: Optional[str] = None

    @property
    def subtotal_cents(self) -> int:
        """Calculate line item subtotal in cents after applying discount."""
        gross = self.quantity * self.unit_price_cents
        discount_Factor = 1.0 - (self.discount_percent / 100.0)
        return round(gross * discount_Factor)
