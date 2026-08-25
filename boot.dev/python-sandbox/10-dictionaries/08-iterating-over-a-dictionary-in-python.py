# * for key in dict: walks *keys*, not values. Then dict[key] is the value.
# * JS: for (const name in obj)  — here `in` actually matches (object keys).
# ?
# ? fruit_sizes = {"apple": "small", "banana": "large"}
# ? for name in fruit_sizes:
# ?     size = fruit_sizes[name]
# ?
# ? Running max again (find-max), but keep the *name* that owns the count.
# ? Start count at -inf, name at None. Empty dict → loop never runs → None.
# ?
# ? Use > not >= so a tie keeps the *first* name you already stored.
# ?
# ? max_enemy_name already starts as None. The extra `== None` check
# ? is the same leftover as find-max — empty dict is already handled.
# ?
# ? Ops flavour: which error type showed up most in this scrape?

# * Assignment: return the enemy name with the highest count, or None.

def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    max_enemy_name = None

    for name in enemies_dict:
        if enemies_dict[name] > max_so_far:
            max_so_far = enemies_dict[name]
            max_enemy_name = name

    if max_enemy_name == None:
        return None

    return max_enemy_name


print(get_most_common_enemy({"jackal": 1, "kobold": 2, "soldier": 3, "gremlin": 5}))
print(get_most_common_enemy({}))