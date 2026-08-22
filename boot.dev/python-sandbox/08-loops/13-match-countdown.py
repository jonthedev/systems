# * Countdown: range can go backwards. Third arg is the step (here -1).
# * range(10, 0, -1) → 10, 9, 8, ... 1
# * Stop is exclusive, same as going up: 0 is *not* in the list.
# ?
# ? range(10, 0, -1)     # 10 down to 1
# ? range(10, -1, -1)    # 10 down to 0  (stop must be -1 to include 0)
# ?
# ? JS: for (let i = 10; i > 0; i--)  — same idea, exclusive of 0.
# ?
# ? Ops flavour: drain a retry budget
# ? for attempt in range(3, 0, -1):
# ?     print(f"{attempt} retries left")

# * Assignment: print 10... 9... ... then on 1: "1...Fight!" (same line).
# * continue after Fight! so we don't also hit print(f"{counter}...").
# ? else would also work; continue is the skip-the-rest-of-this-lap version.

def countdown_to_start():
    for counter in range(10, 0, -1):
        if counter == 1:
            print("1...Fight!")
            continue;
        print(f"{counter}...")


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()