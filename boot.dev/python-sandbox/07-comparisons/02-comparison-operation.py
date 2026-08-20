# * A comparison *is* a boolean
# * `5 > 4` does not stay as an expression — it becomes True or False.
# * You can store that in a variable, same as any other value.
# ?
# ? is_bigger = 5 > 4     # is_bigger is True
# ? is_bigger = True      # same result, just written by hand
# ?
# ? JS: const isBigger = 5 > 4   same idea
# ?
# ? Last lesson: return player_1_score > player_2_score  (inline)
# ? This lesson: name the True/False, then return it.

# * Assignment: three equality checks, return in this order:
# ? mustang vs edward, alphonse vs edward, winry vs alphonse

def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = edward_height == alphonse_height
    is_winry_alphonse_same = winry_height == alphonse_height

    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same
