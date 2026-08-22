# * Loop review 2 — why not 0–1000?
# ?
# ? for i in range(0, 1000):
# ?     print(i)
# ?
# ? Prints 0–999. Stop is exclusive: last i is 999, never 1000.
# ? JS: for (let i = 0; i < 1000; i++)  — same "less than", not "less or equal"

# * Q: Why 0–999 and not 0–1000?
# * A: print(i) only happens while i is less than (not equal to) 1000
