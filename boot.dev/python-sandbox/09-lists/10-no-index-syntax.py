# * for item in items: — walk values, no index. Cleaner when you don't need i.
# * The name after `for` is each *value*, not a number.
# * JS: for (const tree of trees)  — `of`, not `in` (JS `in` is keys, different).
# ?
# ? trees = ["oak", "pine", "maple"]
# ? for tree in trees:
# ?     print(tree)          # oak / pine / maple
# ?
# ? Last lesson needed i: item = items[i]. This skips that extra line.
# ? Still use range(len(...)) when you must update items[i] or print the slot.
# ?
# ? Ops flavour: for host in hosts: ping(host)  — you want the name, not 0, 1, 2.

trees = ["oak", "pine", "maple"]
for tree in trees:
    print(tree)
