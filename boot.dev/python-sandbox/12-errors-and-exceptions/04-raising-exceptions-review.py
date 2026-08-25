# * raise — the keyword that *triggers* an exception. JS: throw
# ?
# ? raise Exception("something bad happened")
# ?
# ? "Good code doesn't need to handle errors, it should be error-free"
# ? → False. Networks drop, ids are missing, users type garbage.
# ? Production code is expected to raise and catch, not pretend nothing fails.
# ?
# ? Python will raise some things for you (10/0, KeyError).
# ? You raise the rest when *you* detect a bad state.
# ?
# ? Ops flavour: disk full, host unreachable, row not in the DB —
# ? those are not "you wrote a bug." They are expected failure cases.

try:
    raise Exception("something bad happened")
except Exception as e:
    print(e)
