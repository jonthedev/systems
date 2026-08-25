# * Counter dict: key = name, value = how many times it showed up.
# * `in` on a dict checks *keys*, not values.
# *   "ford" in cars     → True   (key exists)
# *   "camry" in cars    → False  (that's a value)
# ?
# ? First time you see a name: create the key with 1.
# ? Seen it before: += 1. Do not += on a missing key → KeyError.
# ?
# ? ["goblin", "orc", "goblin"] → {"goblin": 2, "orc": 1}
# ?
# ? List `in` walked values. Dict `in` walks keys. Same word, different bag.
# ?
# ? JS: if (name in counts) counts[name] += 1; else counts[name] = 1
# ?
# ? Ops flavour: count error types in a log, or how many times each host
# ? appears in a scrape. collections.Counter exists later; this is the loop.

# * Assignment: tally each enemy name. Guard with `in` before +=.

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
            
    return enemies_dict


print(count_enemies(["goblin", "orc", "goblin", "dragon", "orc", "goblin"]))





