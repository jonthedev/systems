# * Scope
# * A name is only usable where it is in scope.
# * Parameters and variables created inside a function stay inside
# * that function. Outside, they do not exist.

# ? def subtract(x, y):
# ?     return x - y
# ? result = subtract(5, 3)
# ? print(x)
# ? ERROR: name 'x' is not defined
# ?
# ? 5 was assigned to x only for the duration of subtract.
# ? JS: function subtract(x, y) { return x - y }
# ? subtract(5, 3); console.log(x)  // same idea, x is not global

# * Assignment
# * The bug was calling get_max_health(modifier, level).
# * Those names only exist *inside* the function (the parameters).
# * Out here we have my_modifier and my_level — pass those.

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

# don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")
