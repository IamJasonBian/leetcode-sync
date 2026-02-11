# LeetCode Sync

Automated sync of LeetCode submissions for **slenderman73** (639 solved).

## How it works

### Full Sync (requires auth)
Uses [joshcai/leetcode-sync](https://github.com/joshcai/leetcode-sync) to pull all
accepted submissions with source code. Requires valid LeetCode session cookies stored
as repository secrets:

- `LEETCODE_SESSION` — your `LEETCODE_SESSION` cookie value
- `LEETCODE_CSRF_TOKEN` — your `csrftoken` cookie value

**To refresh tokens:**
1. Log into [leetcode.com](https://leetcode.com) in your browser
2. Open DevTools → Application → Cookies → `leetcode.com`
3. Copy `LEETCODE_SESSION` and `csrftoken` values
4. Update them in this repo's Settings → Secrets → Actions

### Public API Sync (no auth)
Uses [alfa-leetcode-api](https://github.com/alfaarghya/alfa-leetcode-api) to pull
public profile data, skill stats, and recent 20 accepted submissions. Accumulates
submissions over time in `data/all_submissions.json`.

## Stats

| Metric | Count |
|--------|-------|
| Total Solved | 639 |
| Easy | 156 |
| Medium | 384 |
| Hard | 99 |

### Languages
| Language | Problems |
|----------|----------|
| Python3 | 502 |
| Java | 185 |
| MySQL | 16 |
| C++ | 12 |
| JavaScript | 6 |
| Bash | 4 |
| Python | 3 |

### Top Skills
| Skill | Solved |
|-------|--------|
| Array | 347 |
| String | 150 |
| Hash Table | 130 |
| Dynamic Programming | 109 |
| Sorting | 105 |
| Depth-First Search | 84 |
| Math | 83 |
| Two Pointers | 75 |
| Tree | 74 |
| Greedy | 63 |
