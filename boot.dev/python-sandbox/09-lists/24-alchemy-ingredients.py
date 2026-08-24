# * Walk the *recipe* (what you need), not the inventory (what you have).
# * `in` from lesson 17: is this required item anywhere in inventory?
# * Two buckets: count of hits, and a new list of misses.
# ?
# ? recipe    = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
# ? inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]
# ? 3 of 4 found → 75.0   missing = ["Unicorn Hair"]
# ?
# ? percentage = (available / len(recipe)) * 100
# ? Do not divide by len(inventory) — extra junk in the bag is not extra credit.
# ?
# ? Original lists stay put. return percent, missing  is a tuple.
# ?
# ? JS: recipe.filter(i => !inventory.includes(i))  and hits / recipe.length
# ?
# ? Ops flavour: required packages vs what's installed. Walk the spec,
# ? report % present and the names still missing.

# * Assignment: % of recipe you have, plus the missing ingredient names.

def check_ingredient_match(recipe, inventory):
    missing_items = []
    available_items = 0
    for item in recipe:
        if item in inventory:
            available_items += 1
        else:
            missing_items.append(item)

    percentage = (available_items / len(recipe)) * 100
    return percentage, missing_items


recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]
percentage, missing = check_ingredient_match(recipe, inventory)
print(percentage, missing)




