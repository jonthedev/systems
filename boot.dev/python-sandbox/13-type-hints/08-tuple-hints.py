# * Tuple hint lists a type *per position*: tuple[str, int]
# * Fixed length, each slot has its own meaning (and often its own type).
# ?
# ? drop: tuple[str, int] = ("Garnet Mark", 2)
# ?  two values:  [0] name (str)   [1] qty (int)
# ?
# ? stats: tuple[int, float, int] = (100, 42.5, 75)
# ?  three values: HP, MP, stamina — 2 and 3 are the usual sizes.
# ?
# ? list[str]     many items, same type, length can grow
# ? tuple[str, int]  a pair: this then that. Not "a list of mixed junk".
# ?
# ? TS: [string, number]  — a tuple type, not string[]
# ? string[] is a list. [string, number] is a pair. Python: tuple[str, int]
# ?
# ? return "Emerald Brome", 1  — the comma makes a tuple. No extra ( ).
# ?
# ? Ops flavour: addr: tuple[str, int] = ("10.0.0.5", 22)
# ? Host then port. Position *is* the schema.

# * Assignment: enemy_level: int, return -> tuple[str, int]. Body unchanged.

def get_loot_drop(enemy_level: int) -> tuple[str, int]:
    if enemy_level > 10:
        return "Emerald Brome", 1

    return "Smokestone Chip", 3


print(get_loot_drop(5))
print(get_loot_drop(12))
