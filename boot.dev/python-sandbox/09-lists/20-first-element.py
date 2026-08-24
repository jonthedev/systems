# * First item is always index 0 — but only if the list has something.
# * Empty list: items[0] → IndexError. Guard with the length first.
# ?
# ? len(items) == 0  → empty, return "ERROR"  (what this lesson asks)
# ? if not items:    → same idea; empty list is falsy in Python
# ?
# ? JS trap: [] is *truthy*. You cannot if (!items). Use items.length === 0
# ?          or items[0] === undefined.
# ?
# ? return stays after the guard so we never index an empty list.
# ?
# ? Ops flavour: first host in the roster — if the roster is empty, don't
# ? pretend hosts[0] exists; return an error string / exit non-zero.

# * Assignment: items[0], or "ERROR" when the list is empty.

def get_first_item(items):
    if len(items) == 0:
        return "ERROR"
        
    return items[0]


print("filled:", get_first_item(["potion", "bread", "sword"]))
print("empty: ", get_first_item([]))