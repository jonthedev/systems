# * Integers vs floats
# * Integer: whole number, no decimal — 3, -3. Same idea as JS number
# * when you never use a fraction, but Python actually *distinguishes*
# * int vs float as types (JS is just Number / later BigInt).
# ?
# ? 2 + 1  →  3     int
# ? 2 - 1  →  1     int
# ? 2 * 2  →  4     int
# ? 3 / 2  →  1.5   float  — / on two ints still gives a float in Python 3
# ? Integer divide (chop the decimal) is //  e.g. 3 // 2 → 1
# ? JS: 3 / 2 is also 1.5. Python's extra is // and that int stays int.

# * Assignment
# ? total_damage  = sum of all five inputs
# ? average_damage = that total / 5  (a float is correct)

def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage
