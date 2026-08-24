# * Walk every slot with an index: for i in range(len(items))
# * Then items[i] is the value at that slot. Same as JS:
# * for (let i = 0; i < items.length; i++) { const item = items[i] }
# ?
# ? Accumulators again: start at 0, += 1 when you see a match.
# ? elif: after a hit, skip the other names. One item can't be both.
# ? return stays *after* the loop so every item gets counted.
# ?
# ? When you don't need i, Python lets you skip the index:
# ? for item in items:          # next lesson: "no-index syntax"
# ? JS: for (const item of items)
# ?
# ? items.count("Potion") exists, but this exercise wants the loop.
# ?
# ? Ops flavour: count how many hosts are "web" vs "db" in a list.

# * Assignment: tally Potion, Bread, and Shortsword while looping.

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    # don't touch above this line

    for i in range(0, len(items)):
        item = items[i]
        if item == 'Potion':
            potion_count += 1
        elif item == 'Bread':
            bread_count +=1
        elif item == 'Shortsword':
            shortsword_count +=1
            

    # don't touch below this line

    return potion_count, bread_count, shortsword_count


items = ["Potion", "Bread", "Shortsword", "Potion", "Leather", "Bread", "Potion"]
print(get_item_counts(items))

