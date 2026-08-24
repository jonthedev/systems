# * `in` — is this value anywhere in the list? True or False.
# * `not in` — the opposite. Same keyword as for item in items, different job:
# *    for x in list  → walk values
# *    x in list      → membership test (no loop you write)
# ?
# ? "banana" in fruits      → True
# ? "banana" not in fruits  → False
# ?
# ? This is the one-liner version of contains_leather_scraps
# ? (the found=False / loop / break). Python does the walk for you.
# ?
# ? JS: topWeapons.includes(weapon)
# ? JS `in` is keys (0, 1, 2...), not values. Don't use `in` on arrays there.
# ?
# ? Ops flavour: if host in hosts:  — is this box in the inventory?

# * Assignment: return True if weapon is in top_weapons.

def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    # don't touch above this line

    return  weapon in top_weapons


print("great axe: ", is_top_weapon("great axe"))
print("butter knife:", is_top_weapon("butter knife"))