# * set1 - set2 → values in the first bag that are *not* in the second.
# * Difference, not arithmetic minus. "grape" stays if only set1 has it.
# ?
# ? {"apple", "banana", "grape"} - {"apple", "banana"} → {"grape"}
# ?
# ? Lists in, set out: set(list) drops duplicates *and* lets you subtract.
# ? first_ids = [1, 1, 2, 3]  second_ids = [2]
# ? → {1, 3}   (one 1, 2 is gone)
# ?
# ? Original lists are unchanged. You build two sets, then a third.
# ? JS: first.filter(id => !secondSet.has(id)) then wrap in a Set.
# ?
# ? Ops flavour: hosts we expected minus hosts that answered ping
# ? = missing boxes.

# * Assignment: IDs in the first list that are not in the second. A set.

def find_missing_ids(first_ids, second_ids):
    id_set1 = set(first_ids)
    id_set2 = set(second_ids)
    return id_set1 - id_set2


print(find_missing_ids([1, 1, 2, 3, 4], [2, 4]))