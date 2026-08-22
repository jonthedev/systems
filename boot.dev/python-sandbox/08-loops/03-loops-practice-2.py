# * Loops practice — change the *start*
# * range(start, stop): first value is start, last is stop - 1.
# * Only the start changed: 0 → 5. Stop is still the `end` argument.
# ?
# ? range(5, 16)  →  5 6 … 15     (not 16)
# ? range(5, 6)   →  5             (only one number: start, then stop)
# ?
# ? JS: for (let i = 5; i < end; i++)
# ? Don't change the stop — tests pass `end` in.

# * Assignment: print from 5 up to (not including) end.

def print_numbers_from_five_to(end):
    for i in range(5, end):
        print(i)


# Don't edit below this line


def test(end):
    print(f"Using input end: {end}")
    print(f"Printing numbers from 5 to {end - 1}:")
    print_numbers_from_five_to(end)
    print("=====================================")


def main():
    test(16)
    test(6)
    test(11)


main()
