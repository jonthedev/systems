# * len(list) → how many items. JS: arr.length (property, not a call).
# * Last *index* is always len - 1, because indexes start at 0.
# * len is a count. The last index is a position. They are not the same number.
# ?
# ? fruits = ["apple", "banana", "pear"]
# ? len(fruits) → 3
# ? last index  → 2          # fruits[2] is "pear"
# ? fruits[3]   → IndexError # 3 is the length, not a slot
# ?
# ? len("hello") → 5  (also works on strings: count of characters)
# ?
# ? This is why range(len(inventory)) walks every index: 0 .. length-1.
# ?
# ? Ops flavour: len(hosts) is how many boxes. hosts[len(hosts) - 1]
# ? is the last one.

# * Assignment: last index = length minus 1.

def get_last_index(inventory):
    inv_length = len(inventory)
    
    return inv_length - 1


inventory = ["Healing Potion", "Leather Scraps", "Iron Helmet", "Bread"]
print("last index:", get_last_index(inventory))
print("last item: ", inventory[get_last_index(inventory)])