# Stage 2: Finding Anything Instantly (`snacks.nvim`)

<!-- Secret grep beacon for Stage 1: STAGE_2_BEACON -->

You made it to Stage 2! Your setup uses **`folke/snacks.nvim`** as a unified, ultra-fast engine for file picking, live ripgrep, file tree exploration, command palettes, and undo history.

---

## Exercise 2.1: The File Explorer (`<Space>e`)

Your config replaces default `netrw` with the **Snacks Explorer**:

1. Press **`<Space>e`** to toggle the File Explorer on the left.
2. When your cursor is inside the Explorer window:
   - Move up/down with `j` and `k`.
   - Press `<Enter>` or `l` on a folder to expand/collapse it, or on a file to open it.
   - Press **`H`** to toggle hidden dotfiles (like `.gitignore`).
   - Press **`a`** to create a new file or folder (end with `/` for a folder).
   - Press **`r`** to rename a file, or **`d`** to delete a file.
   - Press **`?`** inside the explorer to see all explorer shortcuts!
   - Press **`<Space>e`** or **`q`** to close the explorer when you're done.

> **Tip**: If the explorer is open and your cursor is in your code window, you can hop between the explorer and your code using **`<Ctrl-h>`** (left window) and **`<Ctrl-l>`** (right window)!

---

## Exercise 2.2: Your Top-Level Quick Pickers

Try each of these from right here inside this file (press `<Esc>` to close a picker without selecting, or `<Ctrl-j>` / `<Ctrl-k>` / arrow keys to move through results while typing):

- **`<Space><Space>`** — **Smart Find Files**: Combines recent files, open buffers, and project files ranked by frecency. This will be your #1 most-used shortcut!
- **`<Space>/`** — **Fuzzy Search Lines in Current Buffer**: Try pressing `<Space>/` right now and typing `Explorer`—watch it highlight and preview lines in this file!
- **`<Space>,`** (or `<Space>fb` / `<Space>bb`) — **Switch Open Buffers**: Quickly hop back to `README.md` and then press `<Space>,` again to return here!
- **`<Space>p`** — **Command Palette**: Browse all Neovim commands interactively.
- **`<Space>:`** — **Command History**: Search and re-run past `:` commands.

---

## Exercise 2.3: Deep Search & Inspection (`<Space>f...` & `<Space>s...`)

Test these out to see how much power is under `<Space>f` (Find) and `<Space>s` (Search):

| Shortcut | What It Searches | Try This Exercise |
| :--- | :--- | :--- |
| `<Space>ff` | All Files in Project | Type `invoice` to preview the Python service files |
| `<Space>fg` | Live Ripgrep (Text in Project) | Type `calculate_invoice_total` to see every match |
| `<Space>fw` | Grep Word Under Cursor | Put cursor on any word and press `<Space>fw`! |
| `<Space>fr` | Recent Files | See files you opened recently across sessions |
| `<Space>fc` | **Your Neovim Config!** | Opens a picker directly inside `~/.config/nvim` from anywhere! |
| `<Space>sk` | **Search All Keymaps** | Forgot a shortcut? Press `<Space>sk` and type e.g. `diff` or `format`! |
| `<Space>sh` | Search Neovim Help Docs | Type `options` or `treesitter` |
| `<Space>s.` | **Resume Last Picker** | Re-opens your previous search with your exact query intact! |

### Check Off Your Stage 2 Tasks (`<Space>nc`):
- [ ] I opened and closed the File Explorer with `<Space>e`
- [ ] I searched lines in this buffer with `<Space>/`
- [ ] I searched my keymaps with `<Space>sk`
- [ ] I re-opened my last picker with `<Space>s.`

---

## Next Mission → Stage 3: Teleporting Around Code (`src/navigation_teleport.py`)

Let's use **`<Space>fw` (Grep Word Under Cursor)** to jump to Stage 3!

1. Move your cursor onto the word `teleport_engine` on the line right below this:
   Target function: `teleport_engine`
2. With your cursor on `teleport_engine`, press **`<Space>fw`**.
3. You'll see `src/navigation_teleport.py` in the picker—select it and press **`<Enter>`**!
