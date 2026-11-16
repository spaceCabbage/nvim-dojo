# Welcome to the Neovim Dojo (Beginner-to-Pro Interactive Course)

Welcome! This repository is an **interactive, hands-on Neovim training ground** that takes you from **complete beginner** (learning your very first keystrokes and Vim modes) all the way to **power-user workflows** (fuzzy pickers, 2-keystroke teleportation, smart text objects, Go/Python/JS LSP code intelligence, side-by-side AI diff reviews, regex search & replace, and Markdown note-taking).

---

## Prerequisite: Install the Neovim Config First!

For an accurate learning experience where every shortcut, plugin, and exercise in this Dojo works out of the box, use the Neovim configuration from **`spaceCabbage/dotfiles`**:

- **Neovim Config Repo**: <https://github.com/spaceCabbage/dotfiles/tree/arch/nvim>

### Quick Setup (if you don't have it installed yet):
```bash
# 1. Back up any existing Neovim config
mv ~/.config/nvim ~/.config/nvim.bak 2>/dev/null

# 2. Clone spaceCabbage/dotfiles (arch branch) and link the nvim config
git clone -b arch https://github.com/spaceCabbage/dotfiles.git ~/dotfiles
ln -s ~/dotfiles/nvim ~/.config/nvim

# 3. Open this file in Neovim (lazy.nvim will automatically install all plugins!)
nvim README.md
```
*(Optional: Inside Neovim, run `:MasonToolsInstall` once if you want all LSP servers and formatters for Go, Python, JS/TS, and Markdown installed automatically.)*

---

## Course Roadmap (How This Folder Works)

You will learn **inside Neovim itself** by reading and interacting with real Markdown, Python, JavaScript, and Go files. At the bottom of each file is a **"Next Mission"** that teaches you a new way to jump to the next stage without ever closing Neovim:

0. **[README.md](README.md) *(You are here!)*** — Survival Guide, the 4 Modes, `h j k l`, and your `<Space>` Cheat Sheet
1. **[docs/01-vim-foundations.md](docs/01-vim-foundations.md)** — Fast Movement (`w`, `b`, `0`, `$`), Insert Tricks, Undo/Redo, and "Vim Grammar" (`ciw`, `ci"`, `dd`, `yy`)
2. **[docs/02-finding-and-exploring.md](docs/02-finding-and-exploring.md)** — Finding Anything Instantly (`snacks.nvim` File Explorer, Smart Picker, Live Grep, Keymap Search)
3. **[src/navigation_teleport.py](src/navigation_teleport.py)** *(Python)* — Teleporting Around Code (`flash.nvim`, Treesitter Selection, Buffers, Window Splits & Tmux)
4. **[web/editing_gym.js](web/editing_gym.js)** *(JavaScript)* — Editing Superpowers (`mini.ai` argument/quote text objects, `mini.surround`, Line Bubbling, Clipboard Tricks)
5. **[pkg/billing/service.go](pkg/billing/service.go) & [src/services/invoice_service.py](src/services/invoice_service.py)** *(Go & Python)* — Code Intelligence (LSP `gd`, `gr`, `K`, Rename, `blink.cmp` Autocomplete & `conform.nvim` Auto-Formatting)
6. **[src/ai_review_lab.py](src/ai_review_lab.py)** *(Python + Live Git Diffs)* — Reviewing Code & AI Changes (`gitsigns` Hunk Staging/Rejecting, Side-by-Side `Diffview`, Lazygit)
7. **[pkg/worker/dispatcher.go](pkg/worker/dispatcher.go)** *(Go)* — Regex Search & Replace (`rip-substitute` & `grug-far`), Compiler Diagnostics (`Trouble`), Quickfix (`nvim-bqf`) & Todo Comments
8. **[notes/08-markdown-and-zen.md](notes/08-markdown-and-zen.md)** *(Markdown)* — Note-Taking, Prose Mode, Persistent Scratchpads, Zen Mode & Floating Terminal

---

## Lesson 0.1: Don't Panic! Why Can't I Just Type?

Unlike normal editors (like VS Code or Notepad), Neovim has **Modes**.
When you first open a file, you start in **Normal Mode**.

- In **Normal Mode**, your keyboard is a **game controller** for moving around and editing fast—pressing `j` moves your cursor down instead of typing the letter "j".
- Look at the **bottom-left corner** of your screen right now: you'll see a colored badge that says **`NORMAL`**.

> **THE #1 GOLDEN RULE OF NEOVIM**:
> Whenever you aren't sure what mode you're in, or if a popup/menu is open that you want to close, **press `<Esc>` (the Escape key) once or twice**.
> `<Esc>` ALWAYS brings you safely back home to **Normal Mode** (and if you want to quit Neovim completely from Normal mode, type `:qa` and hit `<Enter>`, or tap `<Space>qq`).

---

## Lesson 0.2: Your First Steps (`h`, `j`, `k`, `l`)

Stay in **Normal Mode** (press `<Esc>`). Instead of reaching for the arrow keys or mouse, place your right hand on the keyboard and move with `h`, `j`, `k`, `l`:

- **`h`** → Move **Left**
- **`j`** → Move **Down** *(tip: `j` has a hook pointing down!)*
- **`k`** → Move **Up**
- **`l`** → Move **Right**

*(Note: Arrow keys and mouse scrolling also work in this config, so don't stress while building muscle memory!)*

### Practice Box: Walk Your Cursor Through the Stars!
Use `h`, `j`, `k`, and `l` to walk your cursor from `[START]` to `[FINISH]`:

```text
   [START] ---> * ---> * ---> *
                              |
                              v
   [FINISH] <-- * <--- * <--- *
```

---

## Lesson 0.3: The 4 Modes (Try Switching Right Now!)

Keep your eye on the **`NORMAL`** badge in the bottom-left corner of your screen as you try each mode:

1. **Insert Mode (Typewriter Mode)**:
   - Press **`i`** right now.
   - Look at the bottom-left corner: the badge changes to **`INSERT`**!
   - Now your keyboard types letters normally! Try typing your name on the line below:
     My name is: 
   - When you finish typing, press **`<Esc>`** to return to **`NORMAL`** mode!
   - Press **`<Ctrl-s>`** (hold `Ctrl` and press `s`) to **Save** the file!

2. **Visual Mode (Highlight / Select Mode)**:
   - In Normal mode, press **`v`** and move around with `h`, `j`, `k`, `l` — you are highlighting characters!
   - Or press **`V`** (Shift + v) to highlight **entire lines** at once!
   - Press **`<Esc>`** to cancel selection and return to **`NORMAL`** mode.

3. **Command Mode (`:` Mode)**:
   - In Normal mode, press **`:`** (Shift + semicolon).
   - Your cursor jumps to the very bottom line of the screen where you can run commands like `:w` (save) or `:q` (quit). Press **`<Esc>`** to cancel.

---

## Lesson 0.4: Your Built-In "Cheat Sheet" (`Space` Key)

In this Neovim setup, you have a special **Leader Key** that opens all your custom menus.
**Your Leader Key is `<Space>` (the Spacebar)!**

> **How to read shortcuts in this guide**:
> - **`<Space>ff`** means: *In Normal mode, tap Spacebar, release it, tap `f`, then tap `f`.* (You do NOT hold Spacebar down—just tap the keys one after another!)
> - **`<Ctrl-d>`** means: *Hold down `Ctrl` and press `d`.*
> - **`<Alt-j>`** means: *Hold down `Alt` (or `Option` on Mac) and press `j`.*

### Try Your Cheat Sheet Right Now:
1. Make sure you're in **Normal Mode** (`<Esc>`).
2. Tap **`<Space>`** once and **wait half a second**.
3. A rounded popup appears at the bottom! This plugin is **Which-Key**. It shows every shortcut group so you **never have to memorize them**:
   - Tap **`t`** right now to open the **Toggle** menu, then tap **`c`** to toggle a 100-character vertical ruler column on/off!
   - Tap **`<Space>?`** (Spacebar followed by `?`) to see shortcuts specific to the current file!
4. Put your cursor on each checklist item below and tap **`<Space>nc`** (Space, then `n`, then `c`) to check it off:

- [ ] I know that `<Esc>` always brings me back to `NORMAL` mode
- [ ] I entered `INSERT` mode with `i`, typed my name, and pressed `<Esc>`
- [ ] I saved the file with `<Ctrl-s>`
- [ ] I opened the `<Space>` menu and checked off these boxes with `<Space>nc`!

---

## Next Mission → Stage 1: Vim Foundations (`docs/01-vim-foundations.md`)

Let's open Stage 1 **without closing Neovim**!
1. Make sure you are in **Normal Mode** (press `<Esc>`).
2. Tap **`<Space>`** twice (**`<Space><Space>`**).
3. A smart file-finder popup opens! Type **`01`** and press **`<Enter>`**.
