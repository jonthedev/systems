# * Indexes start at 0, not 1. Same as JS arrays.
# * "First item" = index 0. "Second item" = index 1.
# * Last index is always length - 1.
# ?
# ? names[0] → "Bob"
# ? names[1] → "Lane"      # the *second* person
# ? names[3] → "Breanna"   # 4 items, last index is 3
# ?
# ? JS: names[0] is the same idea. No difference here.
# ?
# ? This is why range(4) is 0, 1, 2, 3 — those *are* the indexes
# ? of a 4-item list. Exclusive stop again: stop at the length.
# ?
# ? Ops flavour: hosts[0] is the first box, not hosts[1].

names = ["Bob", "Lane", "Alice", "Breanna"]
print("index 0 (first):", names[0])
print("index 1 (second):", names[1])
print("index 3 (last):", names[3])
