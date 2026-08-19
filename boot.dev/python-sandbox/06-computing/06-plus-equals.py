# * Plus-equals (in-place operators)
# * Shortcut for "change in place":  x += 1  means  x = x + 1
# * Python has no ++. JS: i++ / ++i. Python: i += 1
# ?
# ? star_rating = 4
# ? star_rating += 1   # 5     same as star_rating = star_rating + 1
# ? star_rating -= 1   # 3
# ? star_rating *= 2   # 8
# ? star_rating /= 2   # 2.0   / still makes a float
# ?
# ? += -= *= /= are *statements*, not expressions.
# ? So this is illegal:  return current_health -= damage
# ? JS: `return currentHealth -= damage` actually works (assignment
# ?     is an expression there). Python: set first, then return.

# * Assignment: subtract damage with -=, then return the new health.

def get_hurt(current_health, damage):
    current_health -= damage
    return current_health
