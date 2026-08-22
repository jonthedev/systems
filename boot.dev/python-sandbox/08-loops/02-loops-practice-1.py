# * Loops practice
# * Same as last lesson: range stop is exclusive.
# * Print 0 through 199 → last number is 199, so stop is 200.
# ?
# ? for i in range(0, 200):
# ?     print(i)
# ?
# ? JS: for (let i = 0; i < 200; i++)
# ? Indent the body. :

# * Assignment: log 0–199.

def print_numbers():
    for i in range(0, 200):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()
