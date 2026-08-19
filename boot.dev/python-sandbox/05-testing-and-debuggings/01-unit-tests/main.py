# * Unit tests (new lesson type)
# * Earlier chapters: pass if the *printed* text matches.
# * From here: Boot.dev's main_test.py *imports* your function,
# * calls it with inputs, and checks the *return* value.
# * Like Vitest: import { totalXp } from './main' then expect(...).
# * We do not copy their test file (see ../README.md).
# ?
# ? You can leave print() in for debugging. The grader no longer
# ? cares about console output — only what you return.
# ? Boot.dev Run = some cases. Submit = all cases (edge cases).

# * Assignment
# ? 100 xp per level. total_xp = (level * 100) + xp_to_add
# ? level 1 + 100 xp → 200
# ? level 2 + 250 xp → 450

def total_xp(level, xp_to_add):
    current_level = level * 100
    total = current_level + xp_to_add
    return total
