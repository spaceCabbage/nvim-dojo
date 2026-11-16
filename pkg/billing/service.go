// =============================================================================
// STAGE 5: Code Intelligence, Autocomplete & Formatting (Go + Python + JS)
// =============================================================================
// Welcome to `pkg/billing/service.go`!
// Your setup configures `gopls` (Go), `pyright` (Python), `ts_ls` (JS/TS),
// `vue_ls`, `lua_ls`, and `marksman` using Neovim's native LSP client +
// `snacks.nvim` pickers + `blink.cmp` + `conform.nvim`.
package billing

import (
	"errors"
	"fmt"
)

// -----------------------------------------------------------------------------
// EXERCISE 5.1: LSP Navigation (`gd`, `gr`, `gI`, `gy`, `K`, `<Space>cs`)
// -----------------------------------------------------------------------------
// Try these shortcuts right now on `LineItem` or `CalculateInvoiceTotal` below:
//   - `K`          -> Hover Documentation popup (press `K` again to focus the
//                     popup window, or move cursor to dismiss).
//   - `gd`         -> Go to Definition! Put your cursor on `LineItem` or
//                     `SubtotalCents` below and press `gd` — it jumps straight
//                     into `pkg/billing/invoice.go`!
//                     Then press `<Ctrl-o>` to jump right back here!
//   - `gr`         -> Find References in a live Snacks Picker (`<Space>cR` also works).
//   - `gI`         -> Go to Implementation (try `gI` on the `Pricer` interface below!).
//   - `gy`         -> Go to Type Definition (`<Space>ct` also works).
//   - `<Space>cs`  -> Document Symbols / Outline (see all structs, interfaces,
//                     and functions in this file in a fuzzy picker!).
//   - `<Space>cS`  -> Workspace Symbols across the entire repository.
//   - `<Space>th`  -> Toggle LSP Inlay Hints on/off.
// -----------------------------------------------------------------------------

// Pricer is an interface implemented by LineItem (try pressing `gI` on Pricer!).
type Pricer interface {
	SubtotalCents() int64
	Summary() string
}

// InvoiceTotals holds the computed breakdown in cents.
type InvoiceTotals struct {
	SubtotalCents   int64
	TaxCents        int64
	GrandTotalCents int64
}

// CalculateInvoiceTotal computes the subtotal, tax, and grand total for items.
func CalculateInvoiceTotal(items []LineItem, taxRate float64) (InvoiceTotals, error) {
	if taxRate < 0 {
		return InvoiceTotals{}, errors.New("tax rate cannot be negative")
	}

	var subtotal int64
	for _, item := range items {
		subtotal += item.SubtotalCents()
	}

	tax := int64(float64(subtotal)*taxRate + 0.5)
	return InvoiceTotals{
		SubtotalCents:   subtotal,
		TaxCents:        tax,
		GrandTotalCents: subtotal + tax,
	}, nil
}

// -----------------------------------------------------------------------------
// EXERCISE 5.2: Project-Wide Rename (`<Space>cr`) & Code Action (`<Space>ca`)
// -----------------------------------------------------------------------------
// 1. Put your cursor on `FormatCurrencyCents` below.
// 2. Press `<Space>cr` (Code Rename).
// 3. Type a new name (like `RenderDollarAmount`) and press `<Enter>` — both the
//    function definition AND its caller in `BuildReceiptBanner` update at once!
// -----------------------------------------------------------------------------

func FormatCurrencyCents(cents int64) string {
	return fmt.Sprintf("$%.2f", float64(cents)/100.0)
}

func BuildReceiptBanner(customer string, items []LineItem) (string, error) {
	totals, err := CalculateInvoiceTotal(items, 0.0825)
	if err != nil {
		return "", err
	}
	return fmt.Sprintf("Customer: %s | Total: %s", customer, FormatCurrencyCents(totals.GrandTotalCents)), nil
}

// -----------------------------------------------------------------------------
// EXERCISE 5.3: Blazing Fast Autocomplete (`blink.cmp` + `nvim-autopairs`)
// -----------------------------------------------------------------------------
// Inside ` DemoAutocomplete` below, open a new line with `o` and type:
//   `item.`
// Watch `blink.cmp` show `Description`, `DiscountPercent`, `Quantity`, `SKU`,
// `SubtotalCents`, `Summary`, `UnitPriceCents` with live type documentation!
//   - `<C-n>` / `<C-p>` -> Select next / previous completion
//   - `<Tab>` or `<CR>` -> Accept completion
//   - `<C-Space>`       -> Manually open completion menu or toggle docs
// -----------------------------------------------------------------------------
func DemoAutocomplete(item LineItem) string {
	// Put cursor here, press `o`, and type `item.`
	return item.Summary()
}

// -----------------------------------------------------------------------------
// EXERCISE 5.4: Auto-Formatting (`conform.nvim` -> `goimports` + `gofumpt`)
// -----------------------------------------------------------------------------
// Look at `UnformattedGoFunc` below — the spacing is intentionally messy!
//   1. Press `<Space>cf` (Format Buffer) OR save the file with `<Ctrl-s>`!
//   2. `conform.nvim` automatically runs `goimports` and `gofumpt` (and in Python
//      it runs `ruff`, in JS/TS/MD it runs `prettier`).
//   3. Want to temporarily disable format-on-save? Press `<Space>tf`!
// -----------------------------------------------------------------------------
func UnformattedGoFunc(   a int,b   int )   int {
	sum:=a+b
	return   sum*2
}

// =============================================================================
// BONUS: Want to see Stage 5 in Python too?
//   Check out `src/services/invoice_service.py` (`<Space>ff` -> `invoice_service.py`)!
//
// NEXT MISSION -> Stage 6: Git & Reviewing AI Changes (`src/ai_review_lab.py`)
// =============================================================================
// I've prepared real Git commits AND unstaged "AI-generated changes" across
// Python (`src/ai_review_lab.py`), Go (`pkg/billing/service.go`), and JS!
//
// Jump to Stage 6 using the **Git Status Picker**:
//   1. Press `<Space>gst` (Git Status Files).
//   2. Preview the modified files right inside the picker!
//   3. Select `src/ai_review_lab.py` and press `<Enter>`!
