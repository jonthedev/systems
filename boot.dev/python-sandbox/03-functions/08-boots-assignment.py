# * Boots assignment (function-call quiz)
# * How many times is calculate_damage called, and where are the
# * results stored?

# ? Called 3 times.
# ? Returns go into stab_damage, slash_damage, fireball_damage.
# ? def is once. Each line with calculate_damage(...) is a call.
# ? Same recipe, different arguments — that is why functions exist.

def calculate_damage(opening_attack, core_damage, finishing_move):
    total = opening_attack + core_damage + finishing_move
    return total


stab_damage = calculate_damage(10, 20, 30)
slash_damage = calculate_damage(5, 10, 15)
fireball_damage = calculate_damage(50, 60, 70)
print(stab_damage)
print(slash_damage)
print(fireball_damage)
