# * Boolean logic: and / or on comparisons (not just True/False literals)
# * and  → both must be True     JS: &&
# * or   → at least one True     JS: ||
# ?
# ? is_dog:  num_legs == 4  and  weight < 100     (both)
# ? cool car: speed > 200  or  is_electric        (either)
# ?
# ? 4 == 4 and 99 < 100  →  True and True   →  True
# ? 3 == 4 and 98 < 100  →  False and True  →  False
# ? 250 > 200 or False   →  True or False   →  True

# * Assignment: attack hits if
# *   (roll is not 1  AND  roll >= armor)   OR   roll is 20
# * Natural 1 always misses. 20 always hits (even if armor > 20).
# ?
# ? One-liner:  return (roll != 1 and roll >= armor) or roll == 20
# ? Same as the if/elif below — you split the two True cases.

def does_attack_hit(attack_roll, armor_class):
    if attack_roll != 1 and attack_roll >= armor_class:
        return True
    elif attack_roll == 20:
        return True
    else:
        return False
