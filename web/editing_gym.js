/**
 * =============================================================================
 * STAGE 4: The Editing Gym — JavaScript Edition (`web/editing_gym.js`)
 * =============================================================================
 * Welcome to `web/editing_gym.js`!
 * Here you'll practice your editing superpowers (`mini.ai`, `mini.surround`,
 * line bubbling, and register tricks) on realistic JavaScript code.
 *
 * Tip: Feel free to edit and break anything!
 *   - `u`          -> Undo
 *   - `<Ctrl-r>`   -> Redo
 *   - `<Space>su`  -> Visual Undo History Tree (powered by Snacks.picker!)
 */

// -----------------------------------------------------------------------------
// WORKOUT 4.1: Smart Text Objects (`mini.ai`)
// -----------------------------------------------------------------------------
// Standard Vim has `ciw` (change inner word). `mini.ai` adds smart text objects:
//   - `q` -> ANY quote (`'`, `"`, or `` ` `` template literals!)
//   - `b` -> ANY bracket (`()`, `[]`, or `{}`)
//   - `a` -> Function ARGUMENT (handles commas & whitespace automatically!)
//   - `f` -> Function call
//   - `n` / `l` -> "Next" or "Last" match on the line/nearby lines!
//
// Try these exercises on `createCheckoutSession` below:
//   1. Put your cursor anywhere on line 34 and type `cinq` (change inside NEXT
//      quote) — it jumps straight inside `"stripe_eu_live"`!
//   2. Put your cursor on `timeoutMs = 5000` and type `daa` (delete around
//      argument — watch it cleanly remove the parameter AND its comma!).
//   3. Put your cursor on `retryCount = 3` and type `cia` (change inside
//      argument) to replace just that parameter!
// -----------------------------------------------------------------------------
export function createCheckoutSession(
  customerId,
  timeoutMs = 5000,
  retryCount = 3,
  currency = "USD",
) {
  const gateway = "stripe_eu_live";
  const endpoint = `https://api.example.com/v1/checkout/${customerId}`;

  return sendPaymentRequest(endpoint, {
    gateway,
    timeoutMs,
    retryCount,
    currency,
  });
}

function sendPaymentRequest(url, options) {
  return { url, ...options, timestamp: Date.now() };
}

// -----------------------------------------------------------------------------
// WORKOUT 4.2: Fast Surround (`mini.surround` using `gs` prefix)
// -----------------------------------------------------------------------------
// Why `gs`? Because `s` is dedicated to Flash Jump!
//   - `gsa` + motion + char -> Add surrounding (e.g., `gsaiw"` wraps word in `"..."`)
//   - `gsd` + char          -> Delete surrounding (e.g., `gsd"` removes surrounding `"`)
//   - `gsr` + old + new     -> Replace surrounding (e.g., `gsr"'` turns `"x"` into `'x'`,
//                              or `gsr"`` turns `"x"` into a JS template literal `` `x` ``!)
//   - `gsh` + char          -> Highlight surrounding brackets/quotes briefly
//
// Try these on `workoutSurround` below:
//   1. Put cursor inside `"convert_me_to_backticks"` and type `gsr"` followed by `` ` ``!
//   2. Put cursor on the word `wrapMeInParens` and type `gsaiw)`!
//   3. Put cursor inside `(["strip_my_brackets"])` and type `gsd]` then `gsd)`!
// -----------------------------------------------------------------------------
export function workoutSurround() {
  const templateCandidate = "convert_me_to_backticks";
  const bareIdentifier = wrapMeInParens;
  const overNested = (["strip_my_brackets"]);
  return { templateCandidate, bareIdentifier, overNested };
}

const wrapMeInParens = 42;

// -----------------------------------------------------------------------------
// WORKOUT 4.3: Moving Lines & Indenting (`<Alt-j>`, `<Alt-k>`, `<`, `>`, `J`)
// -----------------------------------------------------------------------------
// 1. In `middlewareOrder` below, `"1_auth_guard"` is in the wrong spot!
//    Put your cursor on that line and press `<Alt-k>` twice to bubble it to #1!
// 2. Visually select the whole array (`Vi[`) and press `<Alt-j>` / `<Alt-k>` to
//    move multiple lines together!
// 3. While visually selected, press `>` or `<` — notice how your visual selection
//    stays active so you can indent/outdent repeatedly!
// 4. Put your cursor on `const banner =` and press `J` to join the two lines
//    while keeping your cursor locked in place!
// -----------------------------------------------------------------------------
export function workoutLineMovement() {
  const middlewareOrder = [
    "2_rate_limiter",
    "3_csrf_check",
    "1_auth_guard",
    "4_request_logger",
  ];

  const banner = "Welcome to " +
    "the Neovim Dojo!";

  return { middlewareOrder, banner };
}

// -----------------------------------------------------------------------------
// WORKOUT 4.4: Pro Clipboard & Black-Hole Register (`<Space>P` and `<Space>D`)
// -----------------------------------------------------------------------------
// Normally in Vim, pasting over a visual selection (`viwp`) replaces your
// clipboard with the deleted word. Your config solves this:
//   - `<Space>P` (in Visual mode) -> Paste WITHOUT overwriting your clipboard!
//   - `<Space>D` (Normal/Visual)  -> Delete into black-hole register (`"_d`)!
//
// Try it:
//   1. Put cursor on `PROD_API_KEY_999` below and yank it with `yiw`.
//   2. Select `OLD_KEY_A` with `viw` and press `<Space>P`.
//   3. Select `OLD_KEY_B` with `viw` and press `p` — `PROD_API_KEY_999` is STILL
//      in your clipboard!
// -----------------------------------------------------------------------------
export function workoutClipboard() {
  const masterKey = "PROD_API_KEY_999";
  const serviceA = "OLD_KEY_A";
  const serviceB = "OLD_KEY_B";
  return { masterKey, serviceA, serviceB };
}

// -----------------------------------------------------------------------------
// WORKOUT 4.5: Browse Your Undo Tree (`<Space>su`) & Auto-Format (`<Space>cf`)
// -----------------------------------------------------------------------------
// 1. Press `<Space>su` right now to inspect all your edits in the Snacks Undo Tree!
// 2. Press `<Space>cf` (or `<Ctrl-s>`) to run `prettier` on this JS file!
// -----------------------------------------------------------------------------

// =============================================================================
// NEXT MISSION -> Stage 5: Go & Python LSP Intelligence (`pkg/billing/service.go`)
// =============================================================================
// Now let's check out **Go (`gopls`)** and **Python (`pyright`)** LSP features!
// Press `<Space>ff` (or `<Space><Space>`), type `service.go`, and hit `<Enter>`
// to open `pkg/billing/service.go`!
