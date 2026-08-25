# * try runs until it finishes *or* something raises, whichever first.
# * except only runs if try raised. `as e` is the error object.
# ?
# ? try:
# ?     10 / 0
# ? except Exception as e:
# ?     print(e)          # division by zero — process stays alive
# ?
# ? No try/except around a raise → program *crashes*, Python prints
# ? a traceback. There is no except to run. (That was the quiz.)
# ?
# ? JS: uncaught throw → crash + stack trace. Same idea.
# ?
# ? Ops flavour: an uncaught error in a one-shot script is a non-zero
# ? exit. Caught: you log it and maybe skip that host.

try:
    10 / 0
except Exception as e:
    print(e)
