# tes2 — Agent instructions

Python board-game skeleton: hybrid **Chess vs Shogi** on a 9×9 board (`game/` package). No web server, database, or Docker services.

## Development

| Task | Command |
|------|---------|
| Run tests | `python3 -m pytest tests/ -v` |
| Quick smoke demo | `python3 -c "from game.game import Game; g=Game(); print(g); g.move(0,6,0,5); print(g)"` |

**Runtime:** Python 3.12+ (stdlib only for app code).

**Test dependency:** `pytest` (not pinned in repo; installed via VM update script).

**Lint:** No linter or formatter is configured in this repository.

## Branches

- `main` — placeholder (README/LICENSE only).
- `origin/codex/提案アプリ設計（チェスvs将棋）` / local `feature-branch` — application code (`game/`, `tests/`). Check out this branch before running tests or demos.

## Cursor Cloud specific instructions

- **No long-running services.** End-to-end verification is `pytest` plus an optional one-liner demo that prints the board and performs a pawn move.
- **Working directory:** Run all commands from the repository root (`/workspace`). The `game` package is imported as a top-level module (no `pip install -e .` needed).
- **Dependencies:** Only `pytest` is required beyond the Python stdlib. The VM update script runs `pip install pytest`; no `requirements.txt` exists in the repo.
- **Hot reload:** Not applicable — there is no dev server. After dependency changes, re-run `pytest` in a fresh shell if needed.
