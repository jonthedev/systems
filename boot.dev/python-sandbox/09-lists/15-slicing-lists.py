# * Slice: list[start:stop:step] → a *new* list. Source is unchanged.
# * Stop is exclusive, same as range. Step is stride (default 1).
# * JS: arr.slice(start, stop) — also a copy. splice mutates; slice does not.
# * JS has no step; [::2] is a Python trick.
# ?
# ? scores = [50, 70, 30, 20, 90, 10, 50]
# ? scores[1:5:2] → [70, 20]     # start 1, stop 5 (excluded), every 2nd
# ?
# ? numbers[:3]  → first three          # omit start = from the beginning
# ? numbers[3:]  → from index 3 to end
# ? numbers[::2] → even indexes         # 0, 2, 4, ...
# ? numbers[-3:] → last three           # negative = count from the end
# ? numbers[:-1] → all but the last
# ?
# ? Third champion is index 2 (0, 1, 2). So [2:] not [3:].
# ?
# ? Ops flavour: hosts[1:] skip the first. logs[:-1] drop the last line.
# ? hosts[::2] every other box.

# * Assignment: from 3rd-to-end, all-but-last, even indexes. Three lists.

def get_champion_slices(champions):
    
    return champions[2:], champions[:-1], champions[::2]


champions = ["Frodo", "Aragorn", "Legolas", "Gimli", "Sam", "Galadriel"]
from_third, all_but_last, evens = get_champion_slices(champions)
print("from third:   ", from_third)
print("all but last: ", all_but_last)
print("even indexes: ", evens)
