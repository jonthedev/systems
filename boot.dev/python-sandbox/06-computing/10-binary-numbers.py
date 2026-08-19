# * Binary numbers (base 2)
# * Same counting as decimal, but only symbols 0 and 1.
# * Same rule as Algoroq: start at the *right* with 1, each step left double.
# ?    8    4    2    1
# ?    0    1    0    1   →  4 + 1 = 5
# ?
# ? A 1 = count this column. A 0 = skip it.
# ? Need more columns? Keep doubling: 128 64 32 16 8 4 2 1 (a byte).
# ?
# ? Why ops cares: disk/RAM sizes, 255 in CSS, 1024 in "kibi" units.
# ? You already did this on Algoroq — Boot.dev is the same 8-4-2-1 grid.

# * Python (and JS): 0b prefix means "this int is written in binary"
# ? 0b0001  →  1
# ? 0b0101  →  5
# ? 0b1100  →  12
# ? JS: 0b0101 works too. parseInt("0101", 2) is the string version.

# * Q: 1100 in decimal?
# * A: 12     (8 + 4)
# * Q: 1101 in decimal?
# * A: 13     (8 + 4 + 1)
# * Q: largest decimal you can store in 5 binary digits?
# * A: 31     (11111 → 16+8+4+2+1). All 1s = every column on.
# ?    n bits → biggest number is 2^n - 1.  5 bits → 32 - 1 = 31.
