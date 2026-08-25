# * except matches the *type*, not the message string.
# * except ZeroDivisionError  only catches that type (and its kids).
# * raise Exception("zero division") is a generic Exception.
# * The words "zero division" do not make it a ZeroDivisionError.
# ?
# ? try:
# ?     raise Exception("zero division")
# ? except ZeroDivisionError as e:
# ?     print("zero")
# ?
# ? Nothing matches → uncaught → crash + traceback. (That was the quiz.)
# ?
# ? 10 / 0                → ZeroDivisionError  (would print "zero")
# ? raise Exception("...") → Exception         (would *not* hit that except)
# ?
# ? JS: throw new Error("zero division") is not a TypeError either.
# ? The string is the message. The class is what catch looks at.
# ?
# ? Ops flavour: catch FileNotFoundError, not Exception("file not found").
# ? The message is for humans. The type is for the handler.

try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("not a ZeroDivisionError —", e)
