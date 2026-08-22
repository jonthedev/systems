# * range(start, stop, step) — the 3rd arg is how much i changes each time
# * Default step is +1. Use 2 for evens, -1 to count down.
# * Stop is *still* exclusive, even going backwards.
# ?
# ? range(0, 10, 2)   →  0 2 4 6 8      (not 10)
# ? range(3, 0, -1)   →  3 2 1          (not 0)
# ?
# ? JS: for (let i = 0; i < 10; i += 2)
# ?     for (let i = 3; i > 0; i--)
# ?
# ? Going down: start > stop, step negative. Forget -1 and range is empty
# ? (Python won't walk backwards on its own).

# * Assignment: count down from start (included) to just before end.

def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()
