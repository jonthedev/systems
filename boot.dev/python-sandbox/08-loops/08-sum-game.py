# * Sum game — accumulator
# * Start total at 0 *outside* the loop. Each pass add i (not 1).
# * += is the same in-place add from chapter 6.
# ?
# ? Bug:  total += 1     →  1+1+1+1…  (count of iterations)
# ? Fix:  total += i     →  0+1+2+3…  (sum of the numbers)
# ?
# ? range(start, end) still exclusive of end.
# ? sum_of_numbers(0, 5)  →  0+1+2+3+4  = 10
# ?
# ? JS: let total = 0; for (let i = start; i < end; i++) total += i
# ?
# ? If you set total = 0 *inside* the loop, you wipe the sum every time.

# * Assignment: return the sum of i from start up to (not including) end.

def sum_of_numbers(start, end):
    total = 0
    for i in range(start, end):
        total += i
    return total
