# * Build a *new* list: walk the old one backwards, append as you go.
# * Source is unchanged (not items.reverse(), which mutates in place).
# ?
# ? range(len(items) - 1, -1, -1)
# ?   start = last index (len - 1)
# ?   stop  = -1 (exclusive) so 0 *is* included
# ?   step  = -1  — same countdown trick as 10...1 with range(10, 0, -1)
# ?
# ? [1, 2, 3] → indexes 2, 1, 0 → [3, 2, 1]
# ? Empty list: range(-1, -1, -1) is empty → []  (fine)
# ?
# ? Slice version (not this lesson): items[::-1]  — step -1, whole list.
# ? Builtin reversed() also exists; naming a list `reversed` shadows it.
# ?
# ? JS: [...items].reverse()  or a countdown for. arr.reverse() mutates.
# ?
# ? Ops flavour: last-in-first-out of a host list without popping the source.

# * Assignment: loop backwards, append into a new list, return it.

def reverse_list(items):
    reversed_items = []
    for i in range(len(items) - 1, -1, -1):
        reversed_items.append(items[i])

    return reversed_items


print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c", "d"]))