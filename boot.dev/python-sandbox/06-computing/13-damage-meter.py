# * Damage meter (chapter closer)
# * Interns wrote 8,000,000 — commas split arguments in Python (and JS).
# * That's 4 args, not 2. Thousands delimiter is underscore, not comma.
# ?
# ? calculate_dps(8,000,000, 45)   # WRONG — four arguments
# ? calculate_dps(8_000_000, 45)   # OK — one int: eight million
# ?
# ? 8_000_000   →  8000000     same as lesson 07 underscores
# ? JS: 8_000_000 works too. Never 8,000,000 as a number.

# * Assignment: 8 million / 45s, then 10 million / 49s.

def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


main()
