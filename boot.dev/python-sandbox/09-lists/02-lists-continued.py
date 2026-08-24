# * Multi-line lists are the same list. Just easier to read.
# * One item per line when the row gets long or there are many items.
# * Trailing comma after the last item is fine (and handy when you add more).
# ?
# ? Same as JS:
# ? const flowerTypes = [
# ?   "daffodil",
# ?   "rose",
# ? ]
# ?
# ? A list can hold any type — str, int, bool, even other lists.
# ? Mixing types works; keep a list "about one kind of thing" when you can.
# ?
# ? Ops flavour: a long host list is unreadable on one line.
# ? hosts = [
# ?     "web-1",
# ?     "web-2",
# ?     "db-1",
# ? ]

flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum",
]

player_ages = [
    23,
    18,
    31,
    42,
]

print("flower_types:", flower_types)
print("player_ages:", player_ages)
