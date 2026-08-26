# * dict hint needs TWO types: dict[key_type, value_type]
# * First = keys. Second = values.
# ?
# ? item_counts: dict[str, int] = {
# ?     "Wooden Arrow": 30,
# ?     "Small Amethyst": 2,
# ? }
# ?  dict[str, int]  →  keys are str, values are int
# ?
# ? list[str]  one type  (what's in the list)
# ? dict[str, int]  two types  (what you look up with, what you get back)
# ?
# ? Keys you'll see most: str and int. Values: anything.
# ? (Keys have to be hashable — lists can't be keys. Don't sweat that yet.)
# ?
# ? TS: Record<string, number>  or  { [item: string]: number }
# ? Same map idea. Python writes it as dict[str, int].
# ?
# ? Ops flavour: counts: dict[str, int]  — hostname → request count.
# ? Hover a lookup and you already know it's an int, not a mystery object.

# * Assignment: item_counts: dict[str, int], item_name: str, -> int.

def get_item_count(item_counts: dict[str, int], item_name: str) -> int:
    if item_name in item_counts:
        return item_counts[item_name]
    return 0


print(get_item_count({"potion": 3, "sword": 1}, "potion"))
print(get_item_count({"potion": 3, "sword": 1}, "shield"))
