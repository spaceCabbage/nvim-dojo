# nvim-dojo

An interactive, in-editor training ground for mastering Neovim—from modal fundamentals to LSP navigation, Treesitter text objects, multi-file regex replacement, and side-by-side AI diff review.

Built for [**`spaceCabbage/dotfiles`**](https://github.com/spaceCabbage/dotfiles/tree/arch/nvim), and compatible with vanilla Neovim, Kickstart, or LazyVim.

---

## Why Neovim

- **Grammar Over Mouse Miles** — Edit with composable verbs and nouns (`ci"` changes inside quotes, `daa` deletes a function argument, `s` jumps anywhere on screen in two keystrokes). Your hands stay on the home row.
- **Zero Bloat, <30ms Startup** — Instant startup and minimal memory footprint, leaving your RAM and CPU for Docker stacks, compilers, and language servers.
- **Purpose-Built for AI Workflows** — Pair Neovim + `tmux` with terminal AI agents. Disk changes reload automatically, and `Diffview` + `gitsigns` let you inspect, stage, or reject multi-file AI edits hunk by hunk.
- **Identical Everywhere** — The exact same keybindings, plugins, and speed whether you're on a local Arch desktop, macOS, or SSH'd into a headless Linux server over Tailscale.
- **Yours Forever** — Plain Lua configuration. No telemetry, no account lock-in, no unexpected UI rewrites.

---

## Quick Start

### 1. Install Dependencies

Requires **Neovim 0.10+** (0.11+ recommended), `git`, `ripgrep`, `fd`, `fzf`, and a [Nerd Font](https://www.nerdfonts.com/).

| Platform | Command |
| :--- | :--- |
| **Arch Linux** | `sudo pacman -S neovim git ripgrep fd fzf lazygit` |
| **Debian / Ubuntu** | `sudo apt update && sudo apt install -y neovim git ripgrep fd-find fzf` |
| **macOS** | `brew install neovim git ripgrep fd fzf lazygit` |
| **Windows (Winget / WSL2)** | `winget install Neovim.Neovim BurntSushi.ripgrep.MSVC sharkdp.fd` |

### 2. Choose Your Configuration

#### With `spaceCabbage/dotfiles` (Recommended)
Stages 2–8 map directly to the plugins and `<Space>` keymaps in [`spaceCabbage/dotfiles/nvim`](https://github.com/spaceCabbage/dotfiles/tree/arch/nvim):

```bash
# Back up any existing config
mv ~/.config/nvim ~/.config/nvim.bak 2>/dev/null

# Clone and link the Neovim config
git clone -b arch https://github.com/spaceCabbage/dotfiles.git ~/dotfiles
mkdir -p ~/.config && ln -s ~/dotfiles/nvim ~/.config/nvim

# Clone the dojo, prepare the Git diff lab, and launch
git clone https://github.com/spaceCabbage/nvim-dojo.git ~/nvim-dojo
cd ~/nvim-dojo && ./setup-dojo.sh
nvim README.md
```

> [!TIP]
> **Already have your own `~/.config/nvim`?**
> Run the dotfiles config in an isolated sandbox without touching your existing setup:
> ```bash
> git clone -b arch https://github.com/spaceCabbage/dotfiles.git /tmp/sc-dots
> ln -s /tmp/sc-dots/nvim ~/.config/nvim-dojo-cfg
> NVIM_APPNAME=nvim-dojo-cfg nvim README.md
> ```

#### Without Dotfiles (Vanilla Neovim / Own Config)
- **Stage 0** (`README.md`) and **Stage 1** (`docs/01-vim-foundations.md`) use 100% native Vim motions and operators—no plugins required.
- **LazyVim / Kickstart** users already share ~90% of the plugin stack (`snacks.nvim`, `flash.nvim`, `mini.ai`, `mini.surround`, `gitsigns`, `trouble`, `conform`, `blink.cmp`).

---

## Curriculum

Every file in this repository is an interactive worksheet. Open `README.md` in Neovim, complete the exercises right inside the buffer, and follow the prompt at the bottom of each file to jump to the next stage.

| Stage | File | Stack | Focus |
| :--- | :--- | :--- | :--- |
| **00** | [`README.md`](README.md) | Markdown | Modal editing, `h j k l`, `<Esc>`, `<Space>` Which-Key, UI toggles |
| **01** | [`docs/01-vim-foundations.md`](docs/01-vim-foundations.md) | Markdown | Word/line motions (`w`, `b`, `0`, `$`), Insert modes, Undo/Redo, `Verb + Noun` grammar |
| **02** | [`docs/02-finding-and-exploring.md`](docs/02-finding-and-exploring.md) | Markdown | `snacks.nvim` file picker, live ripgrep, file explorer, command & keymap search |
| **03** | [`src/navigation_teleport.py`](src/navigation_teleport.py) | Python | `flash.nvim` 2-char jumps, Treesitter selection, remote operators, buffers & splits |
| **04** | [`web/editing_gym.js`](web/editing_gym.js) | JavaScript | `mini.ai` text objects, `mini.surround`, line movement, black-hole register, undo tree |
| **05** | [`pkg/billing/service.go`](pkg/billing/service.go) | Go & Python | Native LSP (`gd`, `gr`, `gI`, `K`), symbol rename, `blink.cmp`, `conform.nvim` formatting |
| **06** | [`src/ai_review_lab.py`](src/ai_review_lab.py) | Python + Git | `gitsigns` hunk staging/resetting, inline diffs, `Diffview` side-by-side review, Lazygit |
| **07** | [`pkg/worker/dispatcher.go`](pkg/worker/dispatcher.go) | Go | `rip-substitute` popup, `grug-far` project search/replace, `Trouble` diagnostics, `nvim-bqf` |
| **08** | [`notes/08-markdown-and-zen.md`](notes/08-markdown-and-zen.md) | Markdown | Prose mode, live Markdown rendering, heading outlines, project scratchpads, Zen mode |

---

## Stage 00: Modal Fundamentals

If you have this file open inside Neovim right now, **your training starts here**.

### 1. The Four Modes

Neovim starts in **Normal Mode**, where keys are navigation and editing commands rather than text input. Look at the statusline badge in the bottom-left corner of your window as you switch modes:

| Mode | Enter With | Exit With | Purpose |
| :--- | :--- | :--- | :--- |
| **Normal** | `<Esc>` | — | Navigate, run operators, trigger `<Space>` menus |
| **Insert** | `i` / `a` / `o` | `<Esc>` | Type text normally |
| **Visual** | `v` (char) / `V` (line) | `<Esc>` | Highlight and select regions of text |
| **Command** | `:` | `<Esc>` | Run ex commands (`:w` save, `:q` quit, `:qa` quit all) |

> [!IMPORTANT]
> **Whenever you feel stuck, press `<Esc>`.** It immediately cancels pending commands, closes popups, and returns you to `NORMAL` mode.

---

### 2. Home-Row Navigation (`h`, `j`, `k`, `l`)

In `NORMAL` mode, navigate through the path below from `[START]` to `[END]` using:
- `h` (left) · `j` (down) · `k` (up) · `l` (right)

```text
   [START] ───► ● ───► ● ───► ●
                              │
                              ▼
   [END]   ◄─── ● ◄─── ● ◄─── ●
```

---

### 3. Insert & Save

1. Move your cursor to the end of the `Handle:` line below.
2. Press **`i`** (or **`A`** to jump straight to the end of the line in `INSERT` mode) and type your name.
3. Press **`<Esc>`** to return to `NORMAL` mode.
4. Press **`<Ctrl-s>`** to save the buffer.

```yaml
Handle: 
```

---

### 4. Leader Key (`<Space>`) & Which-Key

Your Leader key is **`<Space>`**.
In notation like `<Space>ff`, tap the keys sequentially in `NORMAL` mode (`Space`, then `f`, then `f`—do not hold `Space` down).

1. Press **`<Space>`** and pause for 250ms to open the **Which-Key** popup.
2. Press **`<Esc>`** to dismiss it, or press **`<Space>?`** to inspect buffer-local keymaps.
3. Test these workspace toggles right now:

| Keymap | Action |
| :--- | :--- |
| `<Space>tn` | Toggle line numbers |
| `<Space>tr` | Toggle relative line numbers |
| `<Space>tw` | Toggle line wrap |
| `<Space>tc` | Toggle 100-column ruler |
| `<Space>nr` | Toggle live Markdown rendering |
| `<Space>nc` | Toggle Markdown checkbox on current line |

4. Place your cursor on each line below and press **`<Space>nc`**:

- [ ] Switched between `NORMAL`, `INSERT`, and `VISUAL` modes
- [ ] Saved the file with `<Ctrl-s>`
- [ ] Explored the `<Space>` Which-Key popup
- [ ] Toggled these checkboxes with `<Space>nc`

---

## Next Stage → [`docs/01-vim-foundations.md`](docs/01-vim-foundations.md)

Open Stage 01 without leaving Neovim:
1. Ensure you are in `NORMAL` mode (`<Esc>`).
2. Press **`<Space><Space>`** to open the smart file picker.
3. Type **`01`** and press **`<Enter>`**.

---

## License

[The Beer-Ware License (Revision 42)](LICENSE)
