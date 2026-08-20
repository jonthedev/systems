# * if statements
# * Run a block only when the condition is True.
# * Python uses indent + colon, not { }. JS: if (cond) { ... }
# ?
# ? if CONDITION:
# ?     # only this indented block is gated
# ? # this line still runs either way
# ?
# ? Don't forget the : after if.
# ?
# ? return inside the if *exits the function* — later lines skip.
# ? This assignment does NOT return: "status check complete" must
# ? always print (like a finally / always-log in ops).
# ?
# ? Ops flavour: if disk_percent >= 90: print("full")
# ?              then still print that the check ran.

# * Assignment: print "dead" if health <= 0; always print the complete line.

def print_status(player_health):
    if player_health <= 0:
        print("dead")
    print("status check complete")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()
