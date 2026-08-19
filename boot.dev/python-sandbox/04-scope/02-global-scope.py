# * Global scope
# * Names defined at the top of the file (not inside a def) are global.
# * Functions can *read* those names without extra syntax.
# ? JS: a const at module top is visible inside functions the same way.

# ? pi = 3.14
# ? def get_area_of_circle(radius):
# ?     return pi * radius * radius
# ? pi lives outside the function but get_area_of_circle can still use it.

# * Assignment
# * Only player_level is global. The functions read it to compute stats.
# * Reading a global is fine. Writing to one from inside a function
# * needs the `global` keyword — not this lesson.
# * In real code, prefer passing level in as an argument (lesson 01).
# * This lesson is just "globals exist."

player_level = 4

# Don't touch below this line


def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")
