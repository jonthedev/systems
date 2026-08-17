# * Function review — what runs, in order
# * Defining a function does not run the body. Calling it does.

# ? 1. def area_of_circle(r):
# ?    Recipe saved. Body ignored until a call. r is the parameter name.
# ?
# ? 2. radius = 5
# ?    A variable in the main program. Not inside the function yet.
# ?
# ? 3. area = area_of_circle(radius)
# ?    CALL. Jump into the body. r is set to 5 (the argument).
# ?
# ? 4. pi = 3.14
# ?    Inside the function now.
# ?
# ? 5. result = pi * r * r
# ?    3.14 * 5 * 5 → 78.5
# ?
# ? 6. return result
# ?    Send 78.5 back out. The call expression becomes 78.5.
# ?
# ? 7. that value is stored in area
# ?
# ? 8. print(area)
# ?    78.5

# * JS is the same timeline: function foo(r) { ... } then foo(radius).
# * Parameter = name in the def. Argument = value you pass in.
