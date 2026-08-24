# * Tuple — ordered, *fixed*. Round brackets. You cannot append, pop, or
# * assign to an index. The sealed box vs a list you can rummage in.
# * Mixed types are normal: a small record, not a growing pile.
# ?
# ? dog = ("Fido", 4)
# ? dog[0] → "Fido"
# ? dog[1] = 5            # TypeError — sealed
# ? one = ("Fido",)       # trailing comma *required* for a 1-item tuple
# ?
# ? Unpacking: name, age = dog     # JS: const [name, age] = dog
# ? return a, b  is actually returning a tuple. You already did this
# ? with potion_count, bread_count, shortsword_count.
# ?
# ? List of tuples: heroes[0] is the first hero, heroes[0][1] is their age.
# ?
# ? JS has no tuple. Closest: a 2-item array you promise not to mutate,
# ? or as const. Destructuring is the same idea as unpacking.
# ?
# ? Ops flavour: (host, port), (ok, status_code) — a pair, not a list
# ? you grow. The slots mean something (name vs age vs is_elf).

# * Assignment: each hero is one tuple (name, age, is_elf), in a list.

def get_heroes():
    heroes = [
        ("Glorfindel",
        2093,
        True,),
        ("Gandalf",
        1054,
        False,),
        ("Gimli",
        389,
        False,),
        ("Aragorn",
        87,
        False)
    ]

    return heroes


print(get_heroes())