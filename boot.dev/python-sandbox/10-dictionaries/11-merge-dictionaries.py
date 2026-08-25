# * Merge: new dict that has every key from both. Second dict wins on clash.
# * Empty {} then copy dict1, then copy dict2 (overwrites matching keys).
# * Originals are unchanged — you build a third dict.
# ?
# ? {"Frodo": 56, "Aragorn": 10} + {"Aragorn": 100, "Gandalf": 809}
# ? → {"Frodo": 56, "Aragorn": 100, "Gandalf": 809}
# ? Aragorn: 10 then 100. Last write wins (same as updating a key).
# ?
# ? for key in dict walks keys; dict[key] is the value (last lesson).
# ? Later: {**dict1, **dict2} or dict1 | dict2. This lesson wants the loops.
# ?
# ? JS: { ...obj1, ...obj2 }  — later keys overwrite. Same rule.
# ?
# ? Ops flavour: default labels, then env-specific labels on top.

# * Assignment: copy dict1, then dict2. Return the merged dict.

def merge(dict1, dict2):
    merged_guild = {}
    for guild in dict1:
        merged_guild[guild] = dict1[guild]

    for key_d2 in dict2:
        merged_guild[key_d2] = dict2[key_d2]

    return merged_guild


two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
print(merge(two_towers, rotk))