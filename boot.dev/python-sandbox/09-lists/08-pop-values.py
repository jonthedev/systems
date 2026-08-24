# * pop() — remove the *last* item and return it. Opposite of append.
# * JS: arr.pop() is the same. The list shrinks by one.
# ?
# ? vegetables = ["broccoli", "cabbage", "kale", "tomato"]
# ? last = vegetables.pop()
# ? # last = "tomato", vegetables = ["broccoli", "cabbage", "kale"]
# ?
# ? pop(1) removes at that *index* (here "cabbage"), not only the end.
# ? JS would be closer to splice(1, 1)[0].
# ?
# ? range(len(inventory)) is computed *once* at the start (6 laps),
# ? so popping inside does not change how many times we loop.
# ? while inventory: item = inventory.pop()  would also drain it.
# ?
# ? Ops flavour: drain a work list from the end until nothing is left.

# * Assignment: each lap, pop the last item into `item` so it can be printed.

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        item = inventory.pop()

        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()