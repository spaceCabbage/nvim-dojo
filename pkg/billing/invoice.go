package billing

import "fmt"

// LineItem represents a single billable item on an invoice.
// Used by `pkg/billing/service.go` in Stage 5 to demonstrate Go LSP (`gopls`).
type LineItem struct {
	SKU             string
	Description     string
	Quantity        int
	UnitPriceCents  int64
	DiscountPercent float64
}

// SubtotalCents returns the discounted total in cents for this line item.
func (item LineItem) SubtotalCents() int64 {
	gross := float64(item.Quantity) * float64(item.UnitPriceCents)
	multiplier := 1.0 - (item.DiscountPercent / 100.0)
	return int64(gross*multiplier + 0.5)
}

// Summary returns a human-readable line item badge.
func (item LineItem) Summary() string {
	dollars := float64(item.SubtotalCents()) / 100.0
	return fmt.Sprintf("%dx %s (%s) = $%.2f", item.Quantity, item.Description, item.SKU, dollars)
}
