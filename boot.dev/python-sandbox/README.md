# Python sandbox

Local copies of Boot.dev Python lessons. The course is still on [Boot.dev](https://www.boot.dev/dashboard) — these files are so you type and run the same ideas on your Mac.

`.py` is Python’s file extension (same idea as `.js` / `.ts`).

## File naming

One file per lesson, so they sort in order:

```
01-print.py
02-variables.py
03-whatever-the-lesson-is.py
```

- Two-digit number (`01`, `02`, … `10`) so `10` does not sort before `2`
- Short topic after a hyphen
- Always `.py`

Re-type the exercise. Do not paste a finished Boot.dev solution in as a second curriculum.

## Comment colors (Better Comments)

Python only has `#`. [Better Comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments) paints the line if a tag sits right after `#`.

House style for this sandbox:

```python
# * general information (green)
# ? important information, or example code (quoted, not executed)
```

Each comment line needs its own tag or it falls back to gray. Real assignment code stays uncommented so `python3` can run it.

## One-time setup (virtualenv)

A venv is like per-project `node_modules`: this folder’s Python packages only.

In Cursor, open a terminal from **Terminal → New Terminal** (or Control + backtick). Click in the terminal so it has focus, then type a command and press **Enter**.

```bash
cd boot.dev/python-sandbox
python3 -m venv venv
source venv/bin/activate
```

When it works, the prompt starts with `(venv)`. Check:

```bash
which python3
```

That path should be inside this folder’s `venv/`, not a system-wide Python.

## Every session

```bash
cd boot.dev/python-sandbox
source venv/bin/activate
python3 01-print.py
```

`python3` is the interpreter. The filename is the script. Output prints in the same terminal.

Swap in the lesson file you are on, e.g. `python3 02-variables.py`.

Leave the venv:

```bash
deactivate
```

## If the terminal does nothing

1. Click inside the terminal (it must be focused).
2. Press **Enter** after the command — typing alone does not run it.
3. If there is no prompt (`%` or `$` or `(venv)`), use **Terminal → New Terminal** and try again.
