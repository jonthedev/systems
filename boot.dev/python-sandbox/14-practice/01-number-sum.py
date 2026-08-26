# * Practice: no new syntax. Accumulator + range + a type hint.
# * Sum 1 through n (inclusive). If n < 1, return 0.
# ?
# ? number_sum(5)  →  1+2+3+4+5  = 15
# ? number_sum(3)  →  1+2+3      = 6
# ? number_sum(0)  →  0          (loop never runs)
# ?
# ? range(1, n) would stop *before* n. We need n included:
# ? range(1, n + 1)  →  1, 2, … n
# ?
# ? count starts at 0 *outside* the loop. Each pass add i, not 1.
# ? (count += 1 would just count how many times you looped.)
# ?
# ? n < 1 is free: range(1, 1) and range(1, 0) are empty.
# ? Empty loop → return the starting 0. No extra if needed.
# ?
# ? JS: let count = 0; for (let i = 1; i <= n; i++) count += i
# ? Note <=  — JS for-loops are often inclusive. range is not.
# ?
# ? Ops flavour: sum of request counts for the last n days.
# ? Day numbers 1..n, same walk.

# * Assignment: add 1..n, return the total (0 if n < 1).

def number_sum(n: int) -> int:
    count: int = 0
    for i in range(1, n + 1):
        count = count + i

    return count


print(number_sum(5))
print(number_sum(3))
print(number_sum(0))
