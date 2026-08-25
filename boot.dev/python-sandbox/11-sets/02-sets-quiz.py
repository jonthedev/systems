# * Quiz recap — set vs list vs dict
# ?
# ? Remove: my_set.remove("apple")
# ? Missing item → KeyError (same loud crash as del dict[key]).
# ? JS: set.delete("apple")  — missing is usually a no-op.
# ?
# ? my_val = {}  → dict, not a set. Empty set is set().
# ?
# ? Good use: the bag of *possible* spells (unique names, `in` checks).
# ? Not a player's spell *order*, not counts (that's a dict).
# ?
# ? .add() to put in. .remove() to take out. Unordered still.
# ?
# ? Ops flavour: allowed_hosts = {"web-1", "db-1"}
# ? if host in allowed_hosts: ...   membership, not a queue.

fruits = {"apple", "banana", "grape"}
fruits.add("pear")
fruits.remove("apple")
print(fruits)
print("empty braces:", type({}))
print("empty set:   ", type(set()))
