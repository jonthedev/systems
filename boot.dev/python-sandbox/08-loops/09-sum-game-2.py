# * Sum of odds — accumulator + step
# * Same total += i as last lesson. Step 2 skips evens.
# * Start at 1 (first odd). Stop is still exclusive of `end`.
# ?
# ? range(1, end, 2)  →  1, 3, 5, …
# ? end=6  →  1+3+5 = 9      (6 not included anyway)
# ? end=5  →  1+3 = 4        (5 is odd but still excluded — stop is exclusive)
# ?
# ? JS: for (let i = 1; i < end; i += 2) total += i

# * Assignment: sum odd numbers from 1 up to (not including) end.

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total
