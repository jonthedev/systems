# * 10 / 0 raises ZeroDivisionError for you. You do not type raise.
# * ZeroDivisionError is a *child* of Exception. except Exception catches it.
# * Quiz: prints "other". Does not crash.
# ?
# ? try:
# ?     10 / 0
# ? except Exception as e:
# ?     print("other")
# ?
# ? Opposite of 06: specific except does NOT catch a general raise.
# ? Here: general except DOES catch a specific raise (the child).
# ?
# ? 06 raise Exception     / except ZeroDivisionError → crash
# ? 07 raise Exception     / except ZDE then Exception → "other"
# ? 08 10/0 (ZDE)          / except Exception          → "other"
# ?
# ? JS: catch (e) catches TypeError too if you don't check instanceof.
# ? except Exception is that wide net.

try:
    10 / 0
except Exception as e:
    print("other")
