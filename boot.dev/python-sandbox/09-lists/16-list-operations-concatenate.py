# * + smushes two lists into a *new* list. Left list first, then right.
# * Originals are unchanged. Not append (that mutates and adds *one* item).
# ?
# ? [1, 2, 3] + [4, 5, 6] → [1, 2, 3, 4, 5, 6]
# ? a + b + c works: just chain them in order.
# ?
# ? JS trap: [1, 2] + [3, 4] becomes the *string* "1,23,4"
# ? JS copy: [...a, ...b] or a.concat(b)
# ?
# ? Ops flavour: all_hosts = web + db + cache  — one list, three sources.

# * Assignment: weapons, then armor, then items. Return the combined list.

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    return favorite_weapons + favorite_armor + favorite_items


weapons = ["shortsword", "bow"]
armor = ["leather", "iron helmet"]
items = ["potion", "bread"]
print(concatenate_favorites(weapons, armor, items))