# * Type hints: write the expected types next to the names.
# * They describe the contract. Python does *not* enforce them at run time.
# ?
# ? weapon: dict   — this param should be a dict
# ? level: int     — this param should be an int
# ? -> int         — this function should return an int
# ?
# ? TS: function getDamage(weapon: Record<string, number>, level: number): number
# ? TS *tsc* can refuse a bad call before run. Python will still run it.
# ? Cursor/Pylance may underline a mismatch — that's a checker, not Python.
# ?
# ? Wrong type at run time: no compile error. Crash only if the body
# ? can't use the value (e.g. "2" + 3 → TypeError). Else it just… works.
# ?
# ? Why bother: readable contracts, editor autocomplete, catch bugs *before*
# ? you run — if you look at the hints / use a checker.
# ?
# ? Ops flavour: def restart(host: str, timeout: int) -> bool
# ? The signature says what you pass, without opening the function body.

# * Assignment: read the hints. They describe expected types.

def get_damage(weapon: dict, level: int) -> int:
    return weapon["damage"] + (level * 2)


sword = {"name": "sword", "damage": 10}
print(get_damage(sword, 3))
