# * "Ordered" = insertion order: the order you *added* the keys.
# * Not alphabetical. Not sorted by value. First in, first when you loop.
# ?
# ? enemies = {"jackal": 1, "kobold": 2, "gremlin": 5}
# ? for name in enemies:  → jackal, then kobold, then gremlin
# ?                        (the order you typed), not gremlin/jackal/kobold
# ?
# ? Python 3.7+: that order is guaranteed every run.
# ? Before 3.7: unordered — loop order could shuffle. "First on a tie"
# ? in get_most_common_enemy would have been luck.
# ?
# ? Lookup is still by *key*. Order does not change enemies["kobold"].
# ? Order only matters when you iterate (for name in dict).
# ?
# ? Lists were always ordered (slot 0, 1, 2). Dicts gained that later.
# ? JS objects: modern engines also keep insertion order for string keys.
# ?
# ? Ops flavour: a config dict prints the keys in the order you defined
# ? them, which makes diffs and logs less chaotic.

enemies = {"jackal": 1, "kobold": 2, "gremlin": 5}
print("insertion order:", list(enemies))
print("alphabetical:   ", sorted(enemies))
