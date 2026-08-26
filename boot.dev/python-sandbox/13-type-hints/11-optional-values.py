# * | in a hint means "this OR that". Not a bitwise-or of values.
# * int | None  →  an int, or None (no value).
# ?
# ? damage_bonus: int | None
# ?   5     → they have a bonus
# ?   None  → they don't. None is the type NoneType, not the number 0.
# ?
# ? def get_prepared_spell(has_spell: bool) -> str | None:
# ?     if has_spell:
# ?         return "Fireball"
# ?     return None
# ?
# ? -> str         always a string (lying if you sometimes return None)
# ? -> str | None  string *or* missing. Callers must handle both.
# ?
# ? TS: string | null     (Python None ≈ JS null)
# ?     string | undefined  is a close cousin. Python has one: None.
# ?
# ? Not the same as a default *argument* (name: str = "Boot").
# ? Defaults are "you may skip passing it".
# ? | None is "the value itself might be empty".
# ?
# ? Ops flavour: def lookup(host: str) -> str | None
# ? Found: the IP. Missing: None — not a fake "0.0.0.0".

# * Assignment: has_mount: bool, distance: int, -> str | None. Body unchanged.

def summon_mount(has_mount: bool, distance: int) -> str | None:
    if not has_mount:
        return None

    if distance > 420:
        return None

    return "Battle Horse"


print(summon_mount(False, 10))
print(summon_mount(True, 500))
print(summon_mount(True, 100))
