#!/usr/bin/env bash
# Generates realistic unstaged "AI changes" in src/ai_review_lab.py for Stage 6
# (Gitsigns & Diffview exercises) after cloning the repository.
set -euo pipefail

cd "$(dirname "$0")"

git checkout -- src/ai_review_lab.py 2>/dev/null || true

python3 - <<'PY'
p = "src/ai_review_lab.py"
s = open(p).read()
s = s.replace(
    "    if bucket.current_tokens >= requested:\n        bucket.current_tokens -= requested\n        return True, round(bucket.current_tokens, 2)",
    "    # [AI-CHANGE #1 - GOOD]: Emit warning threshold when bucket drops below 10%\n    if bucket.current_tokens >= requested:\n        bucket.current_tokens -= requested\n        low_watermark = bucket.capacity * 0.10\n        _is_low = bucket.current_tokens <= low_watermark\n        return True, round(bucket.current_tokens, 2)"
)
s = s.replace(
    "def calculate_backoff_seconds(attempt: int) -> int:\n    \"\"\"Exponential backoff with a sane maximum cap.\"\"\"\n    base_delay = 2 ** max(attempt, 0)\n    return min(base_delay, 60)",
    "def calculate_backoff_seconds(attempt: int) -> int:\n    \"\"\"[AI-CHANGE #2 - BAD HALLUCINATION]: Try rejecting this hunk with <Space>gr!\"\"\"\n    # Whoops! AI hardcoded 99999 seconds delay instead of exponential backoff:\n    return 99999"
)
open(p, "w").write(s)
PY

echo "✓ Stage 6 unstaged AI diffs prepared in src/ai_review_lab.py!"
echo "  Run: nvim README.md"
