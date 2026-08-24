# * Index with square brackets: list[i] → the item at that spot.
# * 0 is the first item. Same syntax as JS: arr[1]
# ?
# ? best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
# ? best_languages[0] → "JavaScript"
# ? best_languages[1] → "Go"
# ?
# ? Out of range (e.g. [5] on a 5-item list) → IndexError. Crash, not undefined.
# ? JS would give undefined. Python is stricter.
# ?
# ? Ops flavour: hosts[0] is the first box. hosts[1] is the second.

# * Assignment: Leather Scraps is the second slot → index 1.

def get_leather_scraps():
    inventory = [
        "Healing Potion",
        "Leather Scraps",
        "Iron Helmet",
        "Bread",
        "Shortsword",
    ]

    item_index = 1

    return inventory[item_index]


print(get_leather_scraps())