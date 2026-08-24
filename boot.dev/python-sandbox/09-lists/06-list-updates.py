# * Lists are mutable: assign to an index and that slot changes.
# * inventory[0] = "Leather Armor"  — same as JS: arr[0] = "Leather Armor"
# * The list is still the same object; one item inside it got replaced.
# ?
# ? inventory = ["Leather", "Iron Ore", "Healing Potion"]
# ? inventory[0] = "Leather Armor"
# ? # ["Leather Armor", "Iron Ore", "Healing Potion"]
# ?
# ? if inventory[1] == "Iron Ore":   # Python: parens around the test are optional
# ?
# ? Ops flavour: hosts[1] = "db-1"  — retag the second box, don't rebuild the list.

# * Assignment: second slot is index 1. If it's Iron Ore, smelt it into an Iron Bar.

def smelt_ore(inventory):
    if(inventory[1] == 'Iron Ore'):
        inventory[1] = 'Iron Bar'
    return inventory


before = ["Leather", "Iron Ore", "Healing Potion"]
print("before:", before)
print("after: ", smelt_ore(before))
