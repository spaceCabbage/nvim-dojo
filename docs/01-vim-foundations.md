# Stage 1: Essential Vim Foundations (Speed, Editing & Grammar)

Awesome job! You just used your file picker (`<Space><Space>`) to open a new file!
Before we dive into your advanced plugins, let's learn the **5-minute core Vim toolkit** that makes editing 10x faster than using a mouse.

---

## Exercise 1.1: Moving Faster Than `h j k l`

Moving one letter at a time with `h` and `l` is too slow for real coding. Stay in **Normal Mode** (`<Esc>`) and try these on the practice sentence below:

- **`w`** → Jump forward to the **start of the next word**
- **`b`** → Jump **back** to the start of the previous word
- **`e`** → Jump to the **end** of the word
- **`0`** (zero) → Jump to the **very beginning** of the line
- **`$`** → Jump to the **very end** of the line

```text
Practice jumping across these words with w, b, e, then jump to the start with 0 and end with $!
```

### Big Jumps Across the File:
- **`<Ctrl-d>`** (hold Control + press `d`) → Scroll **Down** half a screen (and keeps your cursor centered!)
- **`<Ctrl-u>`** (hold Control + press `u`) → Scroll **Up** half a screen
- **`gg`** (tap `g` twice) → Jump to the **very top** of the file
- **`G`** (Shift + `g`) → Jump to the **very bottom** of the file
- **Relative Line Numbers**: Look at the numbers on the left edge of your screen. The line your cursor is on shows its real line number, while lines above/below show **how many lines away they are** (`1, 2, 3...`). Want to jump 6 lines down? Type **`6j`**!

---

## Exercise 1.2: 6 Smart Ways to Enter Insert Mode

You already know **`i`** inserts before the cursor. Here are the other ways pros enter Insert mode (remember to press **`<Esc>`** after each one!):

| Key | Where It Starts Typing | Try It Below! |
| :--- | :--- | :--- |
| **`i`** | **I**nside / before the cursor | Good for mid-word fixes |
| **`a`** | **A**fter the cursor | Great when cursor is on the last letter |
| **`I`** (Shift+i) | At the **very beginning** of the line | No need to press `0` first! |
| **`A`** (Shift+a) | At the **very end** of the line | Huge time-saver for adding `;` or `,`! |
| **`o`** | Opens a **new line BELOW** and enters Insert mode | Try `o` on any line, then `<Esc>`! |
| **`O`** (Shift+o) | Opens a **new line ABOVE** and enters Insert mode | Try `O` on any line, then `<Esc>`! |

### Try `A` and `o` right here:
1. Put your cursor anywhere on the line below and press **`A`** (Shift + a) to type `DONE!` at the end, then press **`<Esc>`**:
   Add text to the end of this line -> 
2. Now press **`o`** to open a brand new line underneath it, type anything, and press **`<Esc>`**.

---

## Exercise 1.3: Undo (`u`) and Redo (`<Ctrl-r>`)

Made a mistake? Never fear:
- In Normal mode, press **`u`** to **Undo** your last change.
- Press **`<Ctrl-r>`** (Control + r) to **Redo** it.
- **Bonus in your setup**: Even if you close Neovim and come back tomorrow, your undo history is saved on disk! And you can press **`<Space>su`** at any time to browse a visual **Undo History Tree**!

---

## Exercise 1.4: The Secret of "Vim Grammar" (`Verb` + `Noun`)

This is why people love Vim. Editing commands read like short English sentences: **`Verb` + `Noun`**.

### Step A: Meet the 3 Verbs (Operators)
- **`d`** = **Delete** (also cuts into your clipboard!)
- **`c`** = **Change** (deletes the text AND immediately puts you in **Insert mode** so you can type a replacement!)
- **`y`** = **Yank** (Copy to clipboard without deleting)

### Step B: Double a Verb to Act on the Whole Line!
- **`dd`** → Delete the entire current line
- **`yy`** → Copy ("yank") the entire current line
- **`cc`** → Clear the entire current line and start typing in Insert mode
- **`p`** → **Paste** below your cursor (or after your cursor)
- **`x`** → Delete the single character right under your cursor

### Step C: Combine a Verb with **`i`** ("inside") or **`a`** ("around")!
Look at how intuitive these combinations are:
- **`ciw`** = **C**hange **I**nside **W**ord *(deletes the whole word under your cursor—even if your cursor is in the middle of the word—and puts you in Insert mode!)*
- **`diw`** = **D**elete **I**nside **W**ord
- **`yiw`** = **Y**ank (copy) **I**nside **W**ord
- **`ci"`** = **C**hange **I**nside **Double Quotes** `""`
- **`di(`** = **D**elete **I**nside **Parentheses** `()`

### Practice Gym — Try Editing the Lines Below!
*(Remember: after using `c` to change text and typing your new word, press **`<Esc>`** to return to Normal mode! And press **`u`** if you ever want to undo!)*

```python
# 1. Put your cursor anywhere in the middle of `wrong_variable_name` below and type `ciw`
#    Type `user_count` and press <Esc>!
wrong_variable_name = 42

# 2. Put your cursor anywhere inside the quotes below and type `ci"`
#    Type `Hello Neovim!` and press <Esc>!
greeting = "replace this whole sentence in three keystrokes"

# 3. Put your cursor on the DELETE_THIS_LINE below and type `dd`!
DELETE_THIS_LINE = "goodbye!"

# 4. Copy the line below with `yy`, then press `p` to paste a duplicate copy below it!
duplicate_me = "I am cloned!"
```

---

## Exercise 1.5: Searching Inside a File (`/`, `n`, `N`, `<Esc>`)

Want to find a word on the page?
1. In Normal mode, press **`/`**, type `Grammar`, and press **`<Enter>`**.
2. Press **`n`** to jump to the **next** match, or **`N`** (Shift+n) for the **previous** match.
3. Done searching? Press **`<Esc>`** in Normal mode and your yellow search highlights disappear!

### Check Off Your Stage 1 Progress (`<Space>nc`):
- [ ] I moved by words (`w`, `b`), line ends (`0`, `$`), and half-pages (`<Ctrl-d>`, `<Ctrl-u>`)
- [ ] I used `ciw` (change inside word) and `ci"` (change inside quotes)
- [ ] I used `dd` (delete line), `yy` + `p` (copy & paste line), and `u` (undo)

---

## Next Mission → Stage 2: Finding & Exploring (`docs/02-finding-and-exploring.md`)

Pick **any** of these 3 ways to open Stage 2 (`docs/02-finding-and-exploring.md`):
1. **Smart Find**: Tap **`<Space><Space>`**, type **`02`**, and press **`<Enter>`**.
2. **Search Text Across Project**: Tap **`<Space>fg`**, type **`STAGE_2_BEACON`**, and press **`<Enter>`**.
3. **Sidebar File Tree**: Tap **`<Space>e`** to open the File Explorer on the left, move down to `docs/02-finding-and-exploring.md` with `j`/`k`, and press **`<Enter>`**.
