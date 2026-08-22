# * for loops — do the same work many times
# * `for i in range(a, b)`: i takes a, then a+1, … up to but *not* b.
# * Inclusive of a, exclusive of b.  range(0, 10)  →  0 1 2 … 9  (not 10)
# ?
# ? for i in range(0, 10):
# ?     print(i)
# ?
# ? JS:  for (let i = 0; i < 10; i++) { console.log(i) }
# ?      Python's range stop is the same idea as  i < 10
# ?
# ? Indent the body, same as if. Don't forget the :
# ?
# ? Ops flavour: retry a check 5 times — range(0, 5) or range(5)
# ? range(5) is the same as range(0, 5).

# * Assignment: print 0 through 99 → range(0, 100)

def print_numbers():
    for i in range(0, 100):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()
