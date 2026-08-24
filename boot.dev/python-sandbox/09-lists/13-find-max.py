# * Running max: start impossibly low, replace whenever you see something bigger.
# * float("-inf") is "smaller than every real number" — safer than 0
# * (0 would win if all damage is negative).
# ?
# ? [100, 10, 22] → 100
# ? [-3, -20, -1] → -1     # why -inf, not 0
# ? []            → -inf   # loop never runs, start value is the answer
# ?
# ? max_so_far is never None. It starts as -inf. Empty list is already handled.
# ?
# ? JS: let maxSoFar = Number.NEGATIVE_INFINITY
# ? Python also has max(nums), but this lesson wants the walk.
# ?
# ? Ops flavour: hottest CPU in a scrape — start at -inf, keep the larger reading.

# * Assignment: walk nums, keep the largest, return it (or -inf if empty).

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num

    return max_so_far


print("positives:", find_max([100, 10, 22]))
print("negatives:", find_max([-3, -20, -1]))
print("empty:    ", find_max([]))