# * Same raise as 06. Now there is a second except — so it does not crash.
# * ZeroDivisionError still does *not* match (type, not the message).
# * Next handler: except Exception → prints "other".
# ?
# ? try:
# ?     raise Exception("zero division")
# ? except ZeroDivisionError as e:
# ?     print("zero")     # skipped — wrong type
# ? except Exception as e:
# ?     print("other")    # matches. Quiz answer.
# ?
# ? 06 = only the specific except → crash
# ? 07 = specific first, then Exception → "other"
# ? Specific still first (05). Exception is the leftover net.
# ?
# ? JS: catch (e) { if (e instanceof ZeroDivisionError) ... else ... }
# ?
# ? Ops flavour: try the specific FileNotFoundError, then a generic
# ? handler for everything else.

try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")
