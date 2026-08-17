# * Parameters vs Arguments
# * Parameter: the name in the def (the slot).
# * Argument:  the actual value you pass when you call.
# ?
# ? a and b are parameters. 5 and 6 are arguments.
# ? People mix the words. In interviews, this split is the precise one.
# ? Same in JS: function add(a, b)  vs  add(5, 6)

def add(a, b):
    return a + b

total = add(5, 6)
print(total)
