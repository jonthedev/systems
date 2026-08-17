# * Functions
# * Functions allow us to reuse and organize code. For example, say we have some code that calculates the area of a circle:
# * circle does not scale. Define once, call many times.

# ? def area_of_circle(r):
# ?     pi = 3.14
# ?     result = pi * r * r
# ?     return result
# ?
# ? r is the parameter (input name).
# ? Indented lines after : are the body (JS uses { } instead).
# ? return is the output — same word as JavaScript.
# ?
# ? area = area_of_circle(5)  # 5 is the argument (the actual value)
# ? print(area)  # 78.5
# ?
# ? JS: function areaOfCircle(r) { return 3.14 * r * r }
# ? Python: def area_of_circle(r): return 3.14 * r * r
# ? Call looks the same: area_of_circle(5)

# * Assignment
# ? Use the given function. Capture sword and spear areas.

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

sword_length = 1.0
spear_length = 2.0

# ? don't touch above this line
sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# ? don't touch below this line
print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")
