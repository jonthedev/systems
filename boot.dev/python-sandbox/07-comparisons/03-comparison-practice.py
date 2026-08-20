# * Comparison practice
# * Store the True/False, or return it directly — same result.
# ?
# ? car_size = 4
# ? truck_size = 5
# ? is_smaller = car_size < truck_size   # True
# ?
# ? >=  means "at least this much" (equal counts as yes)
# ? >   means "strictly more" (equal is no)

# * Assignment: armor withstands the blow if armor >= damage.

def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage
