// =============================================================================
// STAGE 7: Search & Replace, Diagnostics (Trouble) & Quickfix (`nvim-bqf`)
// =============================================================================
// Welcome to `pkg/worker/dispatcher.go`!
// Here you'll learn how to do lightning-fast regex Search & Replace (both inside
// a single file and across the entire repo), plus how to navigate Diagnostics,
// Trouble panels, Quickfix lists, and TODO comments.
package worker

import (
	"fmt"
	"time"
)

// TODO: Stage 7 Landmark #1 — Try pressing `]t` and `[t` to hop between
//       TODO, FIXME, NOTE, and HACK comments in this file!

// -----------------------------------------------------------------------------
// EXERCISE 7.1: Single-File Popup Search & Replace (`<Space>sf` — RipSubstitute)
// -----------------------------------------------------------------------------
// Notice how `legacyDispatchJob` is called multiple times below?
// Let's test `nvim-rip-substitute` (`<Space>sf`):
//   1. Put your cursor on `legacyDispatchJob` (or visually select a block of lines).
//   2. Press `<Space>sf` (Search & Replace in File Popup).
//   3. A sleek floating window opens at the top!
//      - Move between the Search line and Replace line in Normal mode with `j`/`k`,
//        enter Insert mode (`i` or `a`) to type your replacement (e.g. `modernDispatchJob`),
//        and watch the matches highlight and preview LIVE in your buffer!
//      - Press `<Enter>` in Normal mode inside the popup to apply, or `q` / `<Esc>` to cancel!
// -----------------------------------------------------------------------------

type JobPayload struct {
	ID        string
	QueueName string
	Attempts  int
	CreatedAt time.Time
}

func legacyDispatchJob(job JobPayload) string {
	return fmt.Sprintf("[DISPATCH] queue=%s id=%s attempts=%d", job.QueueName, job.ID, job.Attempts)
}

func RunWorkerBatch(jobs []JobPayload) []string {
	var results []string
	for _, job := range jobs {
		// FIXME: Replace `legacyDispatchJob` calls using `<Space>sf` or `<Space>sw`!
		res := legacyDispatchJob(job)
		results = append(results, res)
	}
	return results
}

// -----------------------------------------------------------------------------
// EXERCISE 7.2: Project-Wide Search & Replace (`<Space>sr`, `<Space>sw`, `<Space>sF`)
// -----------------------------------------------------------------------------
// Need to search and replace across MULTIPLE files in your project?
// Your config uses `MagicDuck/grug-far.nvim`:
//   - `<Space>sr` -> Open GrugFar split pre-filtered to current file extension (`*.go`)!
//   - `<Space>sw` -> Open GrugFar pre-filled with the WORD under your cursor across
//                    the entire project!
//   - `<Space>sF` -> Open GrugFar scoped to the current file.
//
// Try it:
//   1. Put your cursor on `legacyDispatchJob` above and press `<Space>sw`.
//   2. Type a replacement in the `Replace:` line.
//   3. In GrugFar, you can preview every match, delete lines with `dd` to exclude
//      specific matches, or press `,r` / `<localleader>r` to sync changes, and
//      press **`q`** in Normal mode to close the GrugFar split!
// -----------------------------------------------------------------------------

// -----------------------------------------------------------------------------
// EXERCISE 7.3: Diagnostics & Trouble (`]d`, `[d`, `<Space>cd`, `<Space>x...`)
// -----------------------------------------------------------------------------
// Look at `BrokenQueueMetrics` below — `unusedLatencyMs` is intentionally declared
// and not used so `gopls` reports a real compiler diagnostic error!
//
// Try these diagnostic tools right now:
//   - `]d` and `[d` -> Jump to Next / Previous diagnostic with a floating popup!
//   - `<Space>cd`   -> Show Line Diagnostics in a floating window.
//   - `<Space>xx`   -> Toggle **Trouble** Workspace Diagnostics panel at the bottom!
//                      (Inside Trouble, press `<Enter>` on an item to jump to it,
//                      or `q` / `<Space>xx` to close Trouble.)
//   - `<Space>xw`   -> Toggle Trouble for Current Buffer Diagnostics only.
//   - `<Space>xE`   -> Toggle Trouble filtered to ERRORS only.
//   - `<Space>xs`   -> Toggle Trouble Document Symbols sidebar!
//   - `<Space>xl`   -> Toggle Trouble LSP References/Definitions sidebar on the right!
//   - `<Space>sd`   -> Fuzzy-search Workspace Diagnostics in Snacks Picker!
// -----------------------------------------------------------------------------
func BrokenQueueMetrics(processed int) string {
	// NOTE: Once you've tested `]d` and `<Space>xx` on the error below, you can
	//       delete the `unusedLatencyMs := 42` line with `dd` to make the file clean!
	unusedLatencyMs := 42
	return fmt.Sprintf("Processed %d jobs", processed)
}

// -----------------------------------------------------------------------------
// EXERCISE 7.4: Supercharged Quickfix List (`nvim-bqf` + `<Space>q...`)
// -----------------------------------------------------------------------------
// Your Quickfix list is upgraded by `kevinhwang91/nvim-bqf` with floating syntax
// previews and `fzf` filtering!
//
// How to test it right now:
//   1. Open any Snacks picker—for example press `<Space>fg` and type `func`.
//   2. Press **`<Ctrl-q>`** (or `<Alt-a>` to select all, then `<Ctrl-q>`) to send
//      those search results into the Quickfix List!
//   3. Look at the Quickfix window at the bottom:
//        - Move up/down with `j`/`k` and watch the floating preview window update!
//        - Press `o` to open the entry under cursor (or `O` to open and close quickfix).
//        - Press `zf` inside the quickfix window to interactively filter the list with `fzf`!
//        - From your code window, press `]q` / `[q` to jump to Next / Prev quickfix item!
//        - Press `<Space>qc` to close the Quickfix list (and `<Space>qo` to reopen it).
// -----------------------------------------------------------------------------

// HACK: Final Stage 7 Todo Landmark! Ready for the grand finale?
// =============================================================================
// NEXT MISSION -> Stage 8: Markdown, Notes, Scratchpads & Zen Mode
//                 (`notes/08-markdown-and-zen.md`)
// =============================================================================
// Press **`<Space>nf`** (Find Markdown Notes in Repo) and select
// `notes/08-markdown-and-zen.md`!
