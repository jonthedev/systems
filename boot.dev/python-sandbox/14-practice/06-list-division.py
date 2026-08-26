# * Map, not filter: every item comes through, transformed. Same length.
# * / in Python 3 always gives a float. 6 / 2 is 3.0, not 3.
# ?
# ? divide_list([6, 8, 10], 2)  →  [3.0, 4.0, 5.0]
# ? []                          →  []
# ?
# ? New list, don't mutate nums. Same build-and-append as remove_nonints,
# ? except we always append (no if).
# ?
# ? -> list[float]  because / produces floats, even when it divides evenly.
# ? // would be whole numbers (floor). This lesson wants /.
# ?
# ? calculation is just a name for num / divisor. You could append the
# ? expression directly. Same result.
# ?
# ? TS: nums.map(n => n / divisor)  — map = "new array, same length".
# ?     filter = "maybe drop items". This is map.
# ?
# ? divisor 0 → ZeroDivisionError. This lesson doesn't ask you to catch it.
# ?
# ? Ops flavour: scale a list of millicores or byte counts down by 1024.
# ? Each value converted, list shape unchanged.

# * Assignment: return a new list of num / divisor for each num.

def divide_list(nums: list[int], divisor: int) -> list[float]:
    d_list: list[float] = []

    for num in nums:
        calculation = num / divisor
        d_list.append(calculation)

    return d_list


print(divide_list([6, 8, 10], 2))
print(divide_list([], 2))
