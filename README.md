# Welcome to the Neovim Dojo (`nvim-dojo`)

Welcome to your interactive, hands-on Neovim training ground!
Every file in this repository is part of an **8-stage quest** designed specifically for **your exact Neovim setup**.

> **Notice how this file looks right now!**
> Because of `render-markdown.nvim`, headings, code blocks, tables, bullets, and checkboxes render cleanly in Normal mode. Move your cursor onto any line and watch `anti_conceal` reveal the raw Markdown syntax on that line!

---

## Stage 1: Your "Cheat Code" (`Space` + Which-Key) & Core Ergonomics

Before you memorize anything, you have a built-in cheat code: **Your Leader key is `<Space>`**.

### Exercise 1.1: Summon Which-Key

1. Make sure you are in **Normal mode** (press `<Esc>`).
2. Press `<Space>` once and **wait 250ms**.
3. Look at the rounded popup at the bottom of your screen—all your shortcuts are grouped logically:
   - `<Space>f` → **Find / Files**
   - `<Space>g` → **Git / Diff Review**
   - `<Space>c` → **Code / LSP**
   - `<Space>s` → **Search / Replace**
   - `<Space>b` → **Buffers**
   - `<Space>w` → **Windows**
   - `<Space>n` → **Notes / Markdown**
   - `<Space>x` → **Diagnostics / Trouble**
   - `<Space>t` → **Toggle / Terminal**
   - `<Space>q` → **Quickfix / Quit**
4. Press `<Esc>` to close the popup.
5. Now press `<Space>?` — this shows **Buffer-Local Keymaps** (shortcuts special to whatever file you currently have open!).
6. Try pressing `g`, `[`, `]`, or `z` and pausing to see what those prefixes do!

---

### Exercise 1.2: Centered Scrolling & Search

Your `init.lua` remaps scrolling and search jumps so your eyes never have to hunt for the cursor at the top or bottom of the screen:

1. Press `<Ctrl-d>` (scroll down half a page) and `<Ctrl-u>` (scroll up half a page). Notice how your cursor **stays locked in the center** of the screen (`zz`)!
2. Search for the word ` Dojos` or `Exercise` by typing `/Exercise<Enter>`.
3. Press `n` (next match) and `N` (previous match) — notice each jump also centers the screen!
4. Press `<Esc>` right now in Normal mode — that immediately clears the yellow search highlight (`:nohlsearch`).

---

### Exercise 1.3: Editor & UI Toggles (`<Space>t...`)

Try toggling these live on this file right now:

| Shortcut                   | Action                         | Try It!                                  |
| :------------------------- | :----------------------------- | :--------------------------------------- |
| `<Space>tn`                | Toggle Line Numbers            | Turn numbers off and back on             |
| `<Space>tr`                | Toggle Relative Line Numbers   | Great for `5j` / `8k` jumps              |
| `<Space>tw`                | Toggle Line Wrap               | Wrap/unwrap long lines                   |
| `<Space>tc`                | Toggle 100-char Colorcolumn    | Adds a vertical ruler guide              |
| `<Space>ts`                | Toggle Spell Check             | Highlights typos                         |
| `<Space>nr` or `<Space>tm` | Toggle Markdown Live Rendering | See raw vs. styled Markdown              |
| `<Ctrl-s>`                 | Save File                      | Works in Normal, Insert, or Visual mode! |

---

### Exercise 1.4: Check Off Your Progress!

Put your cursor anywhere on the checklist lines below and press **`<Space>nc`** (Toggle Markdown Checkbox):

- [ ] I opened the `<Space>` Which-Key menu and `<Space>?` buffer keymaps
- [ ] I scrolled with `<Ctrl-d>` / `<Ctrl-u>` and cleared search highlight with `<Esc>`
- [ ] I tried toggling the 100-col ruler (`<Space>tc`) and Markdown rendering (`<Space>nr`)
- [ ] I checked off these boxes using `<Space>nc`!

---

## Next Mission → Stage 2: Finding & Exploring (`docs/02-finding-and-exploring.md`)

Do **not** close Neovim to open the next file! Pick **any** of these 3 ways to jump to Stage 2 right now:

1. **Method A (Smart Find)**: Press **`<Space><Space>`**, type `02`, and hit `<Enter>`.
2. **Method B (Live Grep)**: Press **`<Space>fg`**, type `STAGE_2_BEACON`, and hit `<Enter>`.
3. **Method C (File Explorer)**: Press **`<Space>e`** to open the sidebar tree on the left, navigate to `docs/02-finding-and-exploring.md` with `j`/`k`, and press `<Enter>`.
