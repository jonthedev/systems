# * Combat advantage — set flags, don't return inside the if
# * Last lessons returned from each branch. Here the function *must*
# * return all three booleans at the end. Flip one to True, leave the rest False.
# ?
# ? advantage, disadvantage, evenly_matched = False, False, False
# ? That's unpacking: three names, three values. JS: three separate lets.
# ?
# ? player_power > enemy_defense   →  advantage
# ? player_power == enemy_defense  →  evenly_matched
# ? else (power < defense)         →  disadvantage
# ?
# ? Check > before ==. else covers the leftover (strictly less).
# ? Don't return inside a branch — you'd skip the other two values.

def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched
