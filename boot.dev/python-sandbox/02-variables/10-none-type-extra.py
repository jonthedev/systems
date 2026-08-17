# * None — extra
# * None means the value is not determined yet, e.g. waiting for input.

# ? username = None
# ? username = input("What's your name? ")
# ? JS: start as null, then assign when the user types.

# * The trap: they look the same when printed
# ? "None" is a string. None is empty. Tests fail if you mix them.
# ? type() is how you tell them apart.

str_none = "None"
actual_none = None

print(str_none)  # looks like: None
print(actual_none)  # looks like: None

print(type(str_none))  # <class 'str'>
print(type(actual_none))  # <class 'NoneType'>
