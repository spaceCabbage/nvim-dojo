# Stage 8: Markdown, Note-Taking, Scratchpads, Terminal & Zen Mode

Congratulations on reaching **Stage 8**, the final stage of the Neovim Dojo!
Your config in `lua/plugins/markdown.lua` and `lua/plugins/snacks.lua` turns Neovim into a first-class Markdown note-taking and technical writing environment.

---

## Exercise 8.1: Prose Mode (Smart Wrapping & Visual Line Motion)

Whenever you open a `.md`, `.mdx`, `.txt`, or `gitcommit` file, your config automatically activates **Prose Mode**:

1. **Clean Word Wrapping**: Long paragraphs wrap cleanly at word boundaries (`linebreak = true` + `breakindent = true`) instead of chopping words in half.
2. **Natural `j` / `k` Navigation**: Try pressing `j` and `k` on the long wrapped paragraph below—notice how your cursor moves down **line-by-visual-line** (`gj` / `gk`) instead of skipping over the whole wrapped paragraph!
   > This is an intentionally long wrapped paragraph so you can test pressing `j` and `k` to glide smoothly up and down through the visual wrapped lines of a single Markdown sentence without jumping past the entire block at once.
3. **Built-in Spell Check**: Spell check is automatically enabled for prose files (`spelllang = 'en_us'`).
   - Jump to a misspelled word with **`]s`** (next) and **`[s`** (previous): `teh` `recieve`
   - Put your cursor on `teh` above and press **`z=`** to pick the correct spelling from a numbered list, or **`zg`** to add a technical term to your dictionary!

---

## Exercise 8.2: Your Dedicated Notes Workflow (`<Space>n...`)

Press `<Space>n` and pause to see your **Notes / Markdown** menu:

| Shortcut | Action | Try It Out! |
| :--- | :--- | :--- |
| **`<Space>nf`** | Find Markdown Notes | Lists only `.md`, `.mdx`, and `.txt` files in the project |
| **`<Space>ng`** | Grep Inside Markdown Notes | Full-text search restricted exclusively to your notes/docs! |
| **`<Space>no`** | **Note Headings / Outline** | Uses `marksman` LSP + Snacks Picker to jump to any `# Heading`! |
| **`<Space>nn`** | **Create New Markdown Note** | Prompts for a path (e.g. `notes/ideas`), auto-creates folders & adds `.md`! |
| **`<Space>nc`** | **Toggle Checkbox** | Turns any text/bullet into `- [ ]`, and toggles `- [ ]` ↔ `- [x]`! |
| **`<Space>nr`** | Toggle Live Markdown Render | Switches `render-markdown.nvim` on/off (same as `<Space>tm`) |

### Try `<Space>nc` on all 3 states below:
- Plain bullet item (press `<Space>nc` to turn me into a checkbox!)
- [ ] Unchecked task (press `<Space>nc` to check me off!)
- [x] Completed task (press `<Space>nc` to uncheck me!)

---

## Exercise 8.3: Persistent Project Scratchpads (`<Space>ns` & `<Space>nS`)

Need a quick place to jot down an API payload, a checklist, or a prompt while coding—without cluttering git?

1. Press **`<Space>ns`** (**Toggle Project Scratch Note**).
2. A floating Markdown window opens! Anything you write there is **automatically saved per project/branch** by `snacks.nvim`.
3. Press **`<Space>ns`** (or `q`) to hide it, and press **`<Space>ns`** again anytime to bring it right back!
4. Press **`<Space>nS`** (**Select Scratch Note**) to browse all your scratchpads across projects.

---

## Exercise 8.4: Distraction-Free Zen Mode (`<Space>tz` / `<Space>nz`)

Want to focus on reading a long design doc or writing deep code in the center of your terminal?

1. Press **`<Space>tz`** (or **`<Space>nz`**).
2. Your buffer centers into a clean, 100-column **Zen Mode** layout!
3. Press **`<Space>tz`** (or `q`) to exit Zen Mode back to your normal layout.

---

## Exercise 8.5: Built-in Floating Terminal (`<Space>tt` & `<Esc><Esc>`)

Need to run a quick shell command without leaving Neovim?

1. Press **`<Space>tt`** (**Toggle Terminal**).
2. Run any command (like `git status` or `ls`).
3. While inside the terminal:
   - Press **`<Space>tt`** again to hide the terminal (your shell process stays alive in the background!).
   - Or press **`<Esc><Esc>`** (double Escape) to switch the terminal into Normal mode so you can scroll up, search terminal output with `/`, or yank text with `y`!

---

## Dojo Graduation Checklist (`<Space>nc` to check off!)

- [ ] **Stage 1**: Mastered `<Space>` (Which-Key), centered `<C-d>`/`<C-u>`, and `<Space>t` toggles
- [ ] **Stage 2**: Explored files with `<Space>e`, `<Space><Space>`, `<Space>fg`, `<Space>fw`, and `<Space>sk`
- [ ] **Stage 3**: Teleported with Flash (`s`, `S`, `yr`), hopped references (`]]`/`[[`), and managed splits/buffers
- [ ] **Stage 4**: Edited JS with `mini.ai` (`cinq`, `daa`, `cia`), `mini.surround` (`gsa`, `gsd`, `gsr`), `<Alt-j/k>`, and `<Space>P`
- [ ] **Stage 5**: Navigated Go & Python with LSP (`gd`, `gr`, `gI`, `K`, `<Space>cs`, `<Space>cr`), `blink.cmp`, and `<Space>cf`
- [ ] **Stage 6**: Reviewed AI diffs with `gitsigns` (`]h`, `<Space>gp`, `<Space>gs`, `<Space>gr`) and `Diffview` (`<Space>gd`, `<Space>gh`)
- [ ] **Stage 7**: Replaced text with `<Space>sf` (RipSubstitute) & `<Space>sw` (GrugFar), and inspected Trouble (`<Space>xx`) & Quickfix (`nvim-bqf`)
- [ ] **Stage 8**: Used Markdown Outline (`<Space>no`), Scratchpad (`<Space>ns`), Zen Mode (`<Space>tz`), and Terminal (`<Space>tt`)
