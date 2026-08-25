# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a personal Python learning repository (`Python_Learnings`). It contains standalone scripts written while working through Python fundamentals, organized by day/session (e.g. `Day1/`). There is no build system, package manager, dependency file, or test suite — each script is a self-contained, runnable file.

## Running scripts

Run any script directly with Python 3, e.g.:

```
python3 Day1/day1.py
```

## Structure and conventions

- Each learning session gets its own top-level directory (e.g. `Day1`, `Day2`, ...), containing one or more small `.py` files for that session's exercises.
- Scripts are simple, linear, script-style Python (no classes/modules/packages expected) — keep additions consistent with that style unless the user asks otherwise.
- When adding a new day's exercises, create a new `DayN/` directory following the existing naming pattern rather than adding files to the repo root.
