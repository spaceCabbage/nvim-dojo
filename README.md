# Welcome to the Neovim Dojo (Beginner-to-Pro Interactive Course)

Welcome! This repository is an **interactive, hands-on Neovim training ground** that takes you from **complete beginner** (learning your very first keystrokes and Vim modes) all the way to **power-user workflows** (fuzzy pickers, 2-keystroke teleportation, smart text objects, Go/Python/JS LSP code intelligence, side-by-side AI diff reviews, regex search & replace, and Markdown note-taking).

---

## Why Neovim? (The Pitch)

Why invest a few hours learning a modal terminal editor when VS Code or Cursor exist?

1. **Edit at the Speed of Thought (Vim Grammar)**:
   In normal editors, you constantly reach for the mouse to highlight characters, drag selections, and click menus. In Neovim, editing is a **language** (`ci"` = *change inside quotes*, `daa` = *delete around function argument*, `s` = *teleport anywhere on screen in 2 keystrokes*). Once your fingers learn the grammar, your hands never leave the home row.
2. **Instant Startup, Zero Electron Bloat**:
   Neovim opens in **under 30 milliseconds** and uses a fraction of a gigabyte of RAM—leaving your CPU and memory free for Docker containers, compilers, test suites, and local tools.
3. **Built for the AI Agent Era**:
   When AI coding agents (like Claude Code, Antigravity, or Codex) run in a terminal pane right next to your editor, Neovim + `tmux` is the ultimate cockpit. Files modified on disk by an AI reload instantaneously (`autoread`), and tools like `Diffview` and `gitsigns` let you inspect, stage, or reject AI changes hunk-by-hunk across the repo in seconds.
4. **Identical Everywhere (Local Desktop, SSH, or Headless VPS)**:
   Whether you're on an Arch Linux desktop, a MacBook, or SSH'd into a headless Debian server over Tailscale, your exact editor, keybindings, LSP intelligence, and muscle memory are 100% identical.
5. **You Own Your Tool Forever**:
   No subscription lock-in, no corporate telemetry, and no UI redesigns breaking your workflow. Your entire editor is a tiny folder of clean Lua files that you understand and control.

---

## Installing Neovim (Step-by-Step)

You need **Neovim 0.10+** (0.11+ recommended), `git`, `ripgrep` (`rg`), and `fd` installed on your machine:

### 1. Install the Neovim Binary & CLI Tools

- **Arch Linux**:
  ```bash
  sudo pacman -S neovim git ripgrep fd fzf lazygit
  ```
- **Debian / Ubuntu**:
  ```bash
  sudo apt update && sudo apt install -y neovim git ripgrep fd-find fzf
  ```
  *(Note: If your Debian/Ubuntu repo has an older Neovim `< 0.10`, grab the latest official release tarball or AppImage from <https://github.com/neovim/neovim/releases>.)*
- **macOS (Homebrew)**:
  ```bash
  brew install neovim git ripgrep fd fzf lazygit
  ```
- **Windows (WSL2 strongly recommended, or Winget)**:
  ```powershell
  winget install Neovim.Neovim BurntSushi.ripgrep.MSVC sharkdp.fd
  ```

*(Tip: Install a [Nerd Font](https://www.nerdfonts.com/) like **JetBrainsMono Nerd Font** in your terminal emulator so file icons and statusline symbols render crisply!)*

---

## Choosing Your Setup: With or Without `spaceCabbage/dotfiles`

### Option A (Recommended): Use the `spaceCabbage/dotfiles` Config
Stages 2 through 8 of this Dojo are specifically tailored around the plugins and `<Space>` keybindings in **`spaceCabbage/dotfiles`**:
- **Config Link**: <https://github.com/spaceCabbage/dotfiles/tree/arch/nvim>

```bash
# 1. Back up any existing Neovim config
mv ~/.config/nvim ~/.config/nvim.bak 2>/dev/null
mv ~/.local/share/nvim ~/.local/share/nvim.bak 2>/dev/null

# 2. Clone spaceCabbage/dotfiles (arch branch) and link the nvim config
git clone -b arch https://github.com/spaceCabbage/dotfiles.git ~/dotfiles
mkdir -p ~/.config
ln -s ~/dotfiles/nvim ~/.config/nvim

# 3. Clone this Dojo, generate the Stage 6 Git diffs, and launch Neovim!
git clone https://github.com/spaceCabbage/nvim-dojo.git ~/nvim-dojo
cd ~/nvim-dojo
./setup-dojo.sh
nvim README.md
```
*(When Neovim opens for the first time, `lazy.nvim` will automatically download all plugins in a few seconds. Run `:MasonToolsInstall` inside Neovim anytime to auto-install the Go, Python, JS/TS, and Markdown language servers.)*

### Option B: Use Vanilla Neovim (or Your Own Config / LazyVim / Kickstart)
Want to try Neovim **without** installing the dotfiles first, or already have your own config?
- **Stage 0 (`README.md`) and Stage 1 (`docs/01-vim-foundations.md`) work in 100% stock, out-of-the-box Neovim** (`nvim -u NONE` or default `nvim`)! Every movement (`h j k l`, `w`, `b`, `0`, `$`, `gg`, `G`), mode (`i`, `v`, `V`, `:`), search (`/`, `n`, `N`), and Vim Grammar command (`ciw`, `ci"`, `dd`, `yy`, `p`, `u`, `<Ctrl-r>`) is standard, universal Vim.
- If you use **LazyVim** or **Kickstart.nvim**, ~90% of Stages 2–8 (`<Space>` leader menus, `snacks.nvim`, `flash.nvim`, `mini.ai`, `mini.surround`, `gitsigns`, `trouble`, `conform`, `blink.cmp`) use the exact same plugins and conventions!
- **Want to test `spaceCabbage/dotfiles` temporarily without touching your current `~/.config/nvim`?**
  Neovim has a built-in `NVIM_APPNAME` feature that lets you run a second config side-by-side in total isolation:
  ```bash
  git clone -b arch https://github.com/spaceCabbage/dotfiles.git /tmp/spacecabbage-dots
  ln -s /tmp/spacecabbage-dots/nvim ~/.config/nvim-dojo-cfg
  NVIM_APPNAME=nvim-dojo-cfg nvim README.md
  ```

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
