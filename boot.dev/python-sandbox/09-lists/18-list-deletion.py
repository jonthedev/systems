# * del — remove by index or slice, *in place*. Source list changes.
# * Does not return the item (pop does). Just deletes.
# * Stop on a slice is exclusive, same as always: [1:3] drops indexes 1 and 2.
# ?
# ? nums = [1, 2, 3, 4, 5]
# ? del nums[3]    # drop index 3 → [1, 2, 3, 5]
# ? del nums[1:3]  # drop a slice → [1, 5]
# ? del nums[:]    # empty the list, same object, now []
# ?
# ? del nums[0]    # first item
# ? del nums[-2:]  # last two (from second-last to the end)
# ?
# ? JS: splice mutates. splice(0, 1) / splice(-2, 2)
# ? Python slice copy (nums[1:3]) does *not* delete. del does.
# ?
# ? Ops flavour: drop the first host, drop the last two from the roster.

# * Assignment: delete the first stronghold, then the last two.

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]


castles = ["Rivendell", "Helm's Deep", "Minas Tirith", "Isengard", "Moria"]
print("before:", castles)
trim_strongholds(castles)
print("after: ", castles)