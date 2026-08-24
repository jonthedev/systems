# * list — an ordered bag of items. JS calls this an array.
# * Square brackets, commas between items. Order is kept.
# ?
# ? inventory = ["Healing Potion", "Leather Scraps", "Iron Helmet"]
# ? Mixed types are allowed: [1, "ok", True] — don't lean on that yet.
# ?
# ? JS: const inventory = ["Healing Potion", "Leather Scraps"]
# ? Same brackets. Python just says "list" instead of "array".
# ?
# ? Ops flavour: hosts = ["web-1", "web-2", "db-1"]
# ? A feed, a cart, a move list — same shape: items in a line.

# * Assignment: return the inventory list, Shortsword last.

def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]


# Don't edit below this line


def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")


def main():
    test()


main()