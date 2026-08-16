# * Variables Vary
# * Variables are called "variables" because they can hold any value
# * and that value can change (it varies).

# ? Reassignment overwrites the old value. This prints 20, not 10:
# ? acceleration = 10
# ? acceleration = 20
# ? print(acceleration)

# * Assignment
# * Reduce our hero's health as they take damage.

# ? Before each print(), set player_health to 100 less than it was.
# ? Expected output:
# ? 900
# ? 800
# ? 700
# ? 600

player_health = 1000

# ? reduce by 100 here
player_health = player_health - 100
print(player_health)

# ? and here
player_health = player_health - 100
print(player_health)

# ? and here
player_health = player_health - 100
print(player_health)

# ? and here
player_health = player_health - 100
print(player_health)
