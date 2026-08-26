# * Container hint: Type[inside]  — the box, then what's in the box.
# * list[str]  a list whose items are strings
# * set[str]   a set  whose items are strings
# ?
# ? inventory: list[str] = ["Iron Sword", "Healing Potion"]
# ? unique_items: set[str] = {"Iron Sword", "Healing Potion"]
# ?
# ? list  ordered, duplicates ok, mutable     TS: string[] / Array<string>
# ? set   unordered, unique only              TS: Set<string>
# ? dict  key → value                         TS: Record<K, V> / Map
# ? tuple fixed-length, immutable             TS: [string, number]  (a pair)
# ?
# ? Square brackets = "of". Not an index. list[str] is not list[0].
# ?
# ? Why it matters: list vs list[str].
# ? Bare list says "some list". list[str] says "strings in it".
# ? Hover / autocomplete then know item is a str.
# ?
# ? Ops flavour: hosts: list[str]  — IPs or names, not mixed junk.
# ? Unique names: set[str]  — the type already says "no dupes".

# * Assignment: inventory: list[str], return -> set[str]. Body unchanged.

def get_unique_items(inventory: list[str]) -> set[str]:
    unique_items = set()

    for item in inventory:
        unique_items.add(item)

    return unique_items


print(get_unique_items(["potion", "potion", "sword"]))
