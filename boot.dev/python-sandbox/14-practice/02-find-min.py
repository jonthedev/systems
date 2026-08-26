# * Running min: start impossibly *high*, replace whenever you see something smaller.
# * float("inf") is bigger than every real number. Mirror of find_max's -inf.
# ?
# ? find_min([1, 3, -1, 2])  →  -1
# ? find_min([18, 3, 7, 2])  →  2
# ? find_min([])             →  inf   # loop never runs, start value is the answer
# ?
# ? Why not start at 0?  [-3, -1] would stay 0 — wrong, 0 was never in the list.
# ? inf loses to *every* real number, so the first item always replaces it.
# ?
# ? -> int | float  because the empty case returns inf (a float), not an int.
# ? Don't use min(nums) — this lesson wants the walk.
# ?
# ? JS: let smallest = Number.POSITIVE_INFINITY
# ?     if (num < smallest) smallest = num
# ? Python `if` doesn't need the extra ( ). Harmless if you keep them.
# ?
# ? Ops flavour: lowest disk free % in a scrape — start at inf, keep the smaller reading.

# * Assignment: walk nums, keep the smallest, return it (or inf if empty).

def find_min(nums: list[int]) -> int | float:
    smallest_number: float = float("inf")
    for num in nums:
        if(num < smallest_number):
            smallest_number = num

    return smallest_number


print(find_min([1, 3, -1, 2]))
print(find_min([18, 3, 7, 2]))
print(find_min([]))
