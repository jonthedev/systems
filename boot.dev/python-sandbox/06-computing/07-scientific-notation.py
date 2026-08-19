# * Scientific notation
# * Write a huge/tiny number as:  coefficient + e + how far to move the decimal.
# * e / E means "times 10 to this power". The result is always a *float*.
# ?
# ? 16e3      →  16000.0     e3  = decimal 3 places right (bigger)
# ? 7.1e-2    →  0.071       e-2 = decimal 2 places left  (smaller)
# ? 1.024e18  →  1024000000000000000.0
# ?
# ? JS: 16e3 works the same. Python extra: ints can be any size;
# ?     scientific notation still makes a float (note the .0).

# * Underscores for readability (not commas)
# ? 16_000        →  16000      int
# ? 16_000_000    →  16000000
# ? JS: 16_000 works in modern JS too. Never write 16,000 — that's a syntax error.

# * Assignment: return small / medium / large max players (scientific notation).
# * Pattern: 1.024e18, then 10x → e19, then 10x → e20.

def max_players_on_server():
    small = 1.024e18
    medium = 1.024e19
    large = 1.024e20
    return small, medium, large
