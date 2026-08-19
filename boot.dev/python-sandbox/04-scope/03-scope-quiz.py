# * Scope quiz
# * Same two rules as 01 and 02.

pi = 3.14


def get_area_of_circle(radius):
    area = pi * radius * radius
    return area


# * Q: does get_area_of_circle have access to pi?
# * A: yes. pi is global (defined at the top of the file). Functions can read it.

# * Q: if get_area_of_circle does not return area, can we use area outside?
# * A: no. area is created inside the function, so it is local.
# *     No return → that value never leaves. print(area) out here would error.
# ? JS: function getArea(radius) { const area = pi * radius * radius }
# ? area is not visible after the function returns unless you return it.
